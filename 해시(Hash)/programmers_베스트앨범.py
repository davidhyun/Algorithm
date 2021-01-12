def solution(genres, plays):
    answer = []
    total_plays = {} # {장르: 총 재생 횟수}
    genre_plays = {} # {장르: [(플레이 횟수, 고유번호)]

    # 해시 만들기
    for i in range(len(genres)):
        # dic.get(key, defalut): key값에 대응되는 value를 반환하고 없으면 default값을 반환
        # (default값을 지정해주지않더라도 에러를 발생시키지 않고 None을 반환)
        total_plays[genres[i]] = total_plays.get(genres[i], 0) + plays[i]
        genre_plays[genres[i]] = genre_plays.get(genres[i], []) + [(plays[i], i)]

    # 장르를 총 재생 횟수 기준으로 내림차순 정렬
    sorted_total_plays = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)

    # 재생 횟수 내림차순, 고유번호 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, total) in sorted_total_plays:
        genre_plays[genre] = sorted(genre_plays[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in genre_plays[genre][:2]]

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))