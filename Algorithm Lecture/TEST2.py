# 각 스탭별로 처리할 3x3 서브 윈도를 찾아서 반환한다.
def getSubWindow(inputPuzzle, row, col):  # 2차원 입력 배열, 입력 배열의 현재 행, 입력 배열의 현재 열
    subWindow = []  # 현재 스탭의 3x3 서브 윈도

    ############# 여기부터 코딩 (1) ---------------->

    # # 3X3 비어있는 2차원 배열 생성
    # for i in range(3):
    #     tmpAry = []
    #     for k in range(3):
    #         tmpAry.append(0)
    #     subWindow.append(tmpAry)

    subWindow = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for k in range(3):
            subWindow[i][k] = inputPuzzle[i-1+row][k-1+col]

    ############# <-------------- 여기까지 코딩 (1)
    
    return subWindow


# 3x3 서브 윈도에서 문항에서 제시한 조건에 따른 최대 절대값을 찾는다.
def calcSubWindow(subWindow):  # 3x3 서브 윈도
    retValue = -1  # 조건에 의해 찾은 최대값.

    ############# 여기부터 코딩 (1) ---------------->

    upperlower = subWindow[0][1] - subWindow[2][1]
    leftright = subWindow[1][0] - subWindow[1][2]
    cross1 = subWindow[0][0] - subWindow[2][2]
    cross2 = subWindow[0][2] - subWindow[2][0]

    if upperlower < 0: upperlower *= -1
    if leftright < 0: leftright *= -1
    if cross1 < 0: cross1 *= -1
    if cross2 < 0: cross2 *= -1

    if retValue < leftright : retValue = leftright
    if retValue < upperlower: retValue = upperlower
    if retValue < cross1: retValue = cross1
    if retValue < cross2: retValue = cross2

    ############# <-------------- 여기까지 코딩 (1)

    return retValue


#
# (N-2)x(N-2) 최종 결과 배열의 해당 위치에 최대값을 대입시킨다.
#
# @param outputPuzzle		(N-2)x(N-2) 크기의 최종 결과 배열.
# @param row			입력 배열의 현재 행.
# @param col			입력 배열의 현재 열.
# @param maxAbsValue		결과 배열에 대입할 최대값.
# @return			최대값을 추가한 (N-2)x(N-2) 크기의 최종 결과 배열.
#
def makeNewPuzzle(outputPuzzle, row, col, maxAbsValue):
    outputPuzzle[row - 1][col - 1] = maxAbsValue

    return outputPuzzle


## 전역 변수 선언 부분
inputPuzzle = []  # NxN 크기의 입력 배열.
outputPuzzle = []  # (N-2)x(N-2) 크기의 최종 결과 배열.
puzzleSize = 0  # 배열의 크기.


def main():
    global inputPuzzle, outputPuzzle, puzzleSize

    loadData()  # 2차원 이미지 읽어오기

    ## 원본 출력
    print(' ----- 원본 퍼즐 -----')
    printData(inputPuzzle, puzzleSize)

    ## 퍼즐 연산
    subWindow = []  # 3x3 서브윈도
    maxAbsValue = 0  # 요구사항에 따른 서브윈도의 최대값.

    outputPuzzle = []  # (N-2)x(N-2) 크기의 최종 결과 배열
    for i in range(puzzleSize - 2):
        tmpAry = []
        for k in range(puzzleSize - 2):
            tmpAry.append(0)
        outputPuzzle.append(tmpAry)

    for i in range(1, puzzleSize - 1):
        for k in range(1, puzzleSize - 1):
            subWindow = getSubWindow(inputPuzzle, i, k)  # 3x3 서브 윈도를 찾음.
            print(" -- 찾은 3x3 서브 윈도. --\n")
            printData(subWindow, 3)  # 찾은 서브 윈도를 출력함
            maxAbsValue = calcSubWindow(subWindow)  # 요구사항에 따른 최대값 반환.
            # outputPuzzle에 최대값을 대입시킴.
            outputPuzzle = makeNewPuzzle(outputPuzzle, i, k, maxAbsValue)

    print(" ----- 최종 결과 퍼즐. -----")
    printData(outputPuzzle, puzzleSize - 2)  # (N-2)x(N-2) 크기의배열 출력.


## 함수 선언 부분
def loadData():  # 데이터 불러오기
    global inputPuzzle, outputPuzzle, puzzleSize

    ###########
    # 제공 데이터 세트 1
    # 5x5 데이터.
    ###########
    puzzleSize = 5
    inputPuzzle = \
        [
            [5, 7, 0, 100, 73],
            [35, 23, 4, 90, 33],
            [49, 85, 62, 39, 81],
            [24, 0, 86, 46, 52],
            [27, 7, 8, 33, 0]
        ]

    '''
    ###########
    # 제공 데이터 세트2 (이 부분의 주석을 풀어서, 작성한 코드의 올바른 작동을 확인해 봐도 됩니다.)
    # 6x6 데이터. 
    ###########
    puzzleSize = 6  
    inputPuzzle = \
    [
        [  1,  62,  3,  4,  5,  6 ],
        [  7,  18,  9, 20, 11, 12 ],
        [ 13,  4, 15, 16,  7, 18 ],
        [ 19, 30, 21, 22, 3,  24 ],
        [ 25, 66, 27, 2, 29,  30 ],
        [ 31, 52, 33, 34, 35, 36 ]
     ]
     '''


def printData(puzzle, pSize):
    for i in range(0, pSize):
        for k in range(0, pSize):
            try:
                print("%3d " % puzzle[i][k], end='')
            except:
                pass
        print()
    print()


## 메인 함수 호출 ##
if __name__ == "__main__":
    main()


