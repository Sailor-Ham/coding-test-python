# 프로그래머스 42579 - 베스트앨범

def solution(genres, plays):
    n = len(genres)

    # 속한 노래가 많이 재생된 장르 (장르: 총 플레이수)
    genre_total_play_dict = {}
    # 장르 내에서 많이 재생된 노래(장르: (인덱스, 플레이수))
    genre_index_play_dict = {}

    for i in range(n):
        genre = genres[i]
        play = plays[i]

        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_dict[genre].append([i, play])

    sorted_genre_total_play = sorted(genre_total_play_dict.items(),
                                     key=lambda x: -x[1])

    result = []

    for genre, total_play in sorted_genre_total_play:
        sorted_genre_index_play = sorted(genre_index_play_dict[genre],
                                         key=lambda x: (-x[1], x[0]))
        count = 0

        for index, play in sorted_genre_index_play:
            if count >= 2:
                break

            result.append(index)

            count += 1

    return result


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
