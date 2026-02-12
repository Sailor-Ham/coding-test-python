# 프로그래머스 42579 - 베스트앨범

def solution(genres, plays):
    n = len(genres)

    genre_total_play_dict = {}
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

    album_list = []

    for genre, total_play in sorted_genre_total_play:
        sorted_genre_index_play = sorted(genre_index_play_dict[genre],
                                         key=lambda x: (-x[1], x[0]))
        count = 0

        for index, play in sorted_genre_index_play:
            if count >= 2:
                break

            album_list.append(index)

            count += 1

    return album_list


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
