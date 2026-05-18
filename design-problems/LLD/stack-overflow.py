# https://algomaster.io/learn/lld/design-stack-overflow

'''

Candidate: Should users be able to comment on both questions and answers? And do we need to support nested comments?

Interviewer: Yes, comments are allowed on both questions and answers. However, to keep things simple, we’ll support only flat (non-nested) comments for now.

Candidate: Do we need to implement a user reputation system that changes based on actions like upvotes, downvotes, and accepted answers?

Interviewer: Yes, users should earn or lose reputation based on votes and whether their answer is accepted. The reputation impact may vary depending on whether the vote is on a question or an answer.

Candidate: Should we support features like tagging, searching, and filtering based on tags or keywords?

Interviewer: Yes. Each question can have one or more tags, and the system should support keyword-based search and tag-based filtering.

Functional Requirements
    Users can post questions, answers, and comments on both questions and answers
    Users can upvote or downvote questions and answers. A user can only vote once per post.
    The original poster of a question can accept one answer as the solution.
    Question can have one or more tags
    Users earn or lose reputation points based on upvotes/downvotes on their content and whether their answer is accepted
    Support searching for questions by keywords in the title or body and filtering questions by tags

Non-Functional Requirements
    Consistency: Voting actions and reputation updates should be strongly consistent and reflected immediately.
    Concurrency: The system must gracefully handle high-concurrency scenarios, such as multiple users voting on the same post simultaneously.
    Scalability: The design should be scalable to accommodate a growing number of users, questions, and answers.


Core Entities
    User
    Question
    Answer
    Comment
    Vote
    Tag

'''

from abc import ABC, abstractmethod
from enum import Enum
from threading import Lock
from datetime import datetime


class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1

class EventType(Enum):
    UPVOTE_QUESTION = 1
    DOWNVOTE_QUESTION = 2
    UPVOTE_ANSWER = 3
    DOWNVOTE_ANSWER = 4
    ACCEPT_ANSWER = 5

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reputation = 0
    
    def update_reputation(self, event_type):
        if event_type == EventType.UPVOTE_QUESTION:
            self.reputation += 5
        elif event_type == EventType.DOWNVOTE_QUESTION:
            self.reputation -= 2
        elif event_type == EventType.UPVOTE_ANSWER:
            self.reputation += 10
        elif event_type == EventType.DOWNVOTE_ANSWER:
            self.reputation -= 2
        elif event_type == EventType.ACCEPT_ANSWER:
            self.reputation += 15
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_reputation(self):
        return self.reputation

# Content (Base Abstraction)
class Content(ABC):
    def __init__(self, id, body, author):
        self.id = id
        self.body = body
        self.author = author
        self.created_at = datetime.now()
    
    def get_id(self):
        return self.id
    
    def get_body(self):
        return self.body
    
    def get_author(self):
        return self.author

class Comment(Content):
    def __init__(self, id, body, author):
        super().__init__(id, body, author)

class Post(Content):
    def __init__(self, id, body, author):
        super().__init__(id, body, author)

        self.votes = {}
        self.vote_count = 0
        self.lock = Lock()
        self.observers = []
        self.comments = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, event_type):
        for observer in self.observers:
            observer.update(event_type)

    def add_comment(self, comment):
        self.comments.append(comment)

    def vote(self, user, vote_type):

        with self.lock:

            if user.id == self.author.id:
                raise Exception("Self voting not allowed")

            if user.id in self.votes:
                raise Exception("Duplicate voting not allowed")

            self.votes[user.id] = vote_type

            if vote_type == VoteType.UPVOTE:
                self.vote_count += 1
                if isinstance(self, Question):
                    event_type = EventType.UPVOTE_QUESTION
                else:
                    event_type = EventType.UPVOTE_ANSWER
            else:
                self.vote_count -= 1
                if isinstance(self, Question):
                    event_type = EventType.DOWNVOTE_QUESTION
                else:
                    event_type = EventType.DOWNVOTE_ANSWER
            
            self.notify_observers(event_type)

class Tag:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Question(Post):
    def __init__(self, id, title, body, author, tags):
        super().__init__(id, body, author)

        self.title = title
        self.tags = set(tags)
        self.answers = []
        self.accepted_answer = None

    def add_answer(self, answer):
        self.answers.append(answer)

    def accept_answer(self, answer, user):

        if user.id != self.author.id:
            raise Exception("Only question owner can accept answer")

        self.accepted_answer = answer
        answer.is_accepted = True

    def get_title(self):
        return self.title

    def get_tags(self):
        return self.tags

    def get_answers(self):
        return self.answers

class Answer(Post):
    def __init__(self, id, body, author):
        super().__init__(id, body, author)

        self.is_accepted = False

    def get_is_accepted(self):
        return self.is_accepted

    def set_accepted(self, accepted):
        self.is_accepted = accepted

class Event:
    def __init__(self, event_type, post, user):
        self.event_type = event_type
        self.post = post
        self.user = user

    def get_type(self):
        return self.event_type

    def get_post(self):
        return self.post

    def get_user(self):
        return self.user

class PostObserver(ABC):

    @abstractmethod
    def update(self, event_type):
        pass

class ReputationObserver(PostObserver):
    def __init__(self, user):
        self.user = user

    def update(self, event_type):
        self.user.update_reputation(event_type)

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query):
        pass

class KeywordSearchStrategy(SearchStrategy):
    def __init__(self, questions):
        self.questions = questions

    def search(self, query):
        results = []
        for question in self.questions.values():
            if query.lower() in question.get_title().lower() or query.lower() in question.get_body().lower():
                results.append(question)
        return results

class TagSearchStrategy(SearchStrategy):
    def __init__(self, questions):
        self.questions = questions

    def search(self, tag):
        results = []
        for question in self.questions.values():
            if tag in question.get_tags():
                results.append(question)
        return results

class StackOverflowService:
    def __init__(self):
        self.questions = {}
        self.users = {}

    def ask_question(self, user, title, body, tags):

        question = Question(
            id=len(self.questions) + 1,
            title=title,
            body=body,
            author=user,
            tags=tags
        )

        # Add reputation observer for the question author
        reputation_observer = ReputationObserver(user)
        question.add_observer(reputation_observer)

        self.questions[question.id] = question

        return question

    def post_answer(self, user, question, body):

        answer = Answer(
            id=len(question.answers) + 1,
            body=body,
            author=user
        )

        # Add reputation observer for the answer author
        reputation_observer = ReputationObserver(user)
        answer.add_observer(reputation_observer)

        question.add_answer(answer)

        return answer

    def add_comment(self, user, post, body):

        comment = Comment(
            id=len(post.comments) + 1,
            body=body,
            author=user
        )

        post.add_comment(comment)

    def vote(self, user, post, vote_type):
        post.vote(user, vote_type)


service = StackOverflowService()

user1 = User(1, "Alice")
user2 = User(2, "Bob")

question = service.ask_question(user1, "What is Python?", "I want to know what Python is.", [Tag("programming"), Tag("python")])
answer = service.post_answer(user2, question, "Python is a programming language.")
service.vote(user1, answer, VoteType.UPVOTE)
print(f"User {user2.get_name()} has reputation {user2.get_reputation()}")