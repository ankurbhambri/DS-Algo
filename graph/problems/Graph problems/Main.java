// https://codeforces.com/problemset/problem/1245/D

import java.io.*;
import java.util.*;

public class Main {
    static class Edge implements Comparable<Edge> {
        int u, v;
        long cost;

        Edge(int u, int v, long cost) {
            this.u = u;
            this.v = v;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge other) {
            return Long.compare(this.cost, other.cost);
        }
    }

    static int[] parent;

    // Union-Find: Find with path compression
    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union-Find: Union by assigning root
    static void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int n = Integer.parseInt(br.readLine());
        int[][] coords = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            coords[i][0] = Integer.parseInt(parts[0]);
            coords[i][1] = Integer.parseInt(parts[1]);
        }

        long[] c = new long[n];
        String[] costParts = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            c[i] = Long.parseLong(costParts[i]);
        }

        int[] k = new int[n];
        String[] kParts = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            k[i] = Integer.parseInt(kParts[i]);
        }

        // Prepare edges
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            edges.add(new Edge(0, i + 1, c[i])); // Connect dummy node to city i+1
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long distance = Math.abs(coords[i][0] - coords[j][0]) + Math.abs(coords[i][1] - coords[j][1]);
                long cost = (long) (k[i] + k[j]) * distance;
                edges.add(new Edge(i + 1, j + 1, cost));
            }
        }

        // Sort edges by cost
        Collections.sort(edges);

        // Initialize Union-Find
        parent = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        long totalCost = 0;
        List<Integer> powerStations = new ArrayList<>();
        List<int[]> connections = new ArrayList<>();

        // Kruskal's Algorithm
        for (Edge edge : edges) {
            int u = edge.u;
            int v = edge.v;
            if (find(u) != find(v)) {
                union(u, v);
                totalCost += edge.cost;
                if (u == 0) {
                    powerStations.add(v);
                } else {
                    connections.add(new int[]{u, v});
                }
            }
        }

        // Output the result
        out.println(totalCost);
        out.println(powerStations.size());
        for (int i = 0; i < powerStations.size(); i++) {
            if (i > 0) out.print(" ");
            out.print(powerStations.get(i));
        }
        out.println();
        out.println(connections.size());
        for (int[] connection : connections) {
            out.println(connection[0] + " " + connection[1]);
        }

        out.flush();
        out.close();
    }
}
