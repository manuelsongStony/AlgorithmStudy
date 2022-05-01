def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        if frame[3] == 1:  # 설치
            if (frame[2] == 0):  # 기둥
                if (frame[1] == 0):
                    answer.append([frame[0], frame[1], frame[2]])

                elif ([frame[0], frame[1], 1] in answer  # 한쪽끝부분위에있거나
                      or [frame[0] - 1, frame[1], 1] in answer):
                    answer.append([frame[0], frame[1], frame[2]])

                elif ([frame[0], frame[1] - 1, 0] in answer):
                    answer.append([frame[0], frame[1], frame[2]])

            if frame[2] == 1:  # 보
                if ([frame[0], frame[1] - 1, 0] in answer
                        or [frame[0] + 1, frame[1] - 1, 0] in answer):

                    answer.append([frame[0], frame[1], frame[2]])

                elif ([frame[0] + 1, frame[1], 1] in answer and
                      [frame[0] - 1, frame[1], 1] in answer
                ):

                    answer.append([frame[0], frame[1], frame[2]])

        if frame[3] == 0:  # 삭제
            if frame[2] == 0:  # 기둥

                if ([frame[0], frame[1] + 1, 0] in answer and
                        ([frame[0] - 1, frame[1] + 1, 1] not in answer and
                         [frame[0], frame[1] + 1, 1] not in answer)
                ):

                    pass
                elif ([frame[0], frame[1] + 1, 1] in answer and
                      (([frame[0] - 1, frame[1] + 1, 1] not in answer or
                        [frame[0] + 1, frame[1], 1] not in answer) and
                       [frame[0] + 1, frame[1] + 1, 1] not in answer)):

                    pass
                elif ([frame[0] - 1, frame[1] + 1, 1] in answer and

                      (([frame[0] - 2, frame[1] + 1, 1] not in answer or
                        [frame[0], frame[1], 1] not in answer) and
                       [frame[0] - 1, frame[1] + 1, 1] not in answer)):

                    pass
                else:

                    answer.remove([frame[0], frame[1], frame[2]])

            if frame[2] == 1:  # 보
                if ([frame[0], frame[1], 0] in answer and
                        [frame[0], frame[1] - 1, 0] not in answer
                ):
                    pass
                elif ([frame[0] + 1, frame[1], 0] in answer and
                      [frame[0] + 1, frame[1] - 1, 0] not in answer
                ):
                    pass
                elif ([frame[0] - 1, frame[1], 1] in answer and
                      [frame[0] - 1, frame[1] - 1, 0] not in answer):
                    pass
                elif ([frame[0] + 1, frame[1], 1] in answer and
                      [frame[0] + 1, frame[1] - 1, 0] not in answer):
                    pass
                else:
                    answer.remove([frame[0], frame[1], frame[2]])

    answer.sort(key=lambda x: (int(x[0]), int(x[1])))
    return answer