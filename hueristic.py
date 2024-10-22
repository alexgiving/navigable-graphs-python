import random
from typing import List, Tuple


class Candidate:
    def __init__(self, index, distance, data):
        self.index = index
        self.distance = distance
        self.data = data

    def __lt__(self, other):
        return self.distance < other.distance


class ModifiedHeuristic:
    def __init__(self, candidates, curr, k, distance_func, data, long_edge_ratio=None, dropout_ratio=None):
        self.candidates = [Candidate(index, distance, data[index]) for index, distance in candidates]
        self.k = k
        self.distance_func = distance_func
        self.long_edge_ratio = long_edge_ratio
        self.dropout_ratio = dropout_ratio
        self.result = []
        self.result_indx_set = set()
        self.added_data = {}

    def _get_candidates(self) -> List[Candidate]:
        if self.dropout_ratio:
            total_distance = sum(candidate.distance for candidate in self.candidates)
            num_candidates_to_drop = int(len(self.candidates) * self.dropout_ratio)
            probabilities = [candidate.distance / total_distance for candidate in self.candidates]
            candidates_to_drop = set(random.choices(
                self.candidates,
                weights=probabilities,
                k=num_candidates_to_drop
            ))
            candidates_to_process = [candidate for candidate in self.candidates if candidate not in candidates_to_drop]
            return candidates_to_process
        return self.candidates[1:]

    def find_neighbors(self) -> List[Tuple[int, float]]:
        self.candidates.sort()

        first_candidate = self.candidates[0]
        self.result.append((first_candidate.index, first_candidate.distance))
        self.result_indx_set.add(first_candidate.index)
        self.added_data[first_candidate.index] = first_candidate.data

        for candidate in self._get_candidates():
            if candidate.index in self.added_data:
                continue

            if candidate.distance < min(self.distance_func(candidate.data, self.added_data[added]) for added in self.added_data):
                self.result.append((candidate.index, candidate.distance))
                self.result_indx_set.add(candidate.index)
                self.added_data[candidate.index] = candidate.data

            if len(self.result) >= self.k:
                break

        if self.long_edge_ratio:
            num_long_edges = int(self.k * self.long_edge_ratio)
            far_neighbors = self.candidates[-num_long_edges:]

            for candidate in far_neighbors:
                if candidate.index not in self.result_indx_set:
                    self.result.append((candidate.index, candidate.distance))
                    self.result_indx_set.add(candidate.index)

        return self.result


def modified_heuristic(candidates, curr, k, distance_func, data, long_edge_ratio=0.19, dropout_ratio=0.01):
    heuristic = ModifiedHeuristic(candidates, curr, k, distance_func, data, long_edge_ratio, dropout_ratio)
    return heuristic.find_neighbors()
