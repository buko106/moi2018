from api import APIService
from itertools import product

TOKEN = "<TOKEN>"

digits = "0123456789"
if __name__ == "__main__":
    api_service = APIService(TOKEN)

    level = 4
    all_pattern_set = set(
        "".join(as_tuple)
        for as_tuple in product(digits, repeat=level)
        if len(set(as_tuple)) == level
    )

    hit_blow_query_to_answer_set = {}
    for query, ans in product(all_pattern_set, repeat=2):
        hit = sum(1 for d1, d2 in zip(query, ans) if d1 == d2)
        hit_plus_blow = len(set(query) & set(ans))
        blow = hit_plus_blow - hit
        elem = (hit, blow, query)
        if hit_blow_query_to_answer_set.get(elem) is None:
            hit_blow_query_to_answer_set[elem] = set()
        hit_blow_query_to_answer_set[elem].add(ans)

    answer_set = all_pattern_set.copy()
    api_service.start(level)
    while len(answer_set) >= 1:
        answer = str(answer_set.pop())
        resp_dict = api_service.answer(answer)
        print(resp_dict["message"])
        answer_set &= hit_blow_query_to_answer_set[(resp_dict["hit"], resp_dict["blow"], answer)]