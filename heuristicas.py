#[0,0(1)  - 0,1(2)  - 0,2(3)  - 0,3(4)]
#[1,0(12) - 1,1(13) - 1,2(14) - 1,3(5)]
#[2,0(11) - 2,1(0)  - 2,2(15) - 2,3(6)]
#[3,0(10) - 3,1(9)  - 3,2(8)  - 3,3(7)]


class Position:
	'Contains attribute row and column of a piece on the board'

	def __init__(self, row, column):
		self.row = row;
		self.column = column;


correctAnswer = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7];
correctAnswerMap = {
	1 : 0,  2 : 1,  3 : 2,  4 : 3,
	12: 4,  13: 5,  14: 6,  5 : 7,
	11: 8,  0 : 9,  15: 10, 6 : 11,
	10: 12, 9 : 13, 8 : 14, 7 : 15,
}
correctPositionMap = {
	1 : Position(0, 0),
	2 : Position(0, 1),
	3 : Position(0, 2),
	4 : Position(0, 3),
	12: Position(1, 0),
	13: Position(1, 1),
	14: Position(1, 2),
	5 : Position(1, 3),
	11: Position(2, 0),
	0 : Position(2, 1),
	15: Position(2, 2),
	6 : Position(2, 3),
	10: Position(3, 0),
	9 : Position(3, 1),
	8 : Position(3, 2),
	7 : Position(3, 3),
}
arrayToBoardMap = {
	0 : Position(0, 0),
	1 : Position(0, 1),
	2 : Position(0, 2),
	3 : Position(0, 3),
	4 : Position(1, 0),
	5 : Position(1, 1),
	6 : Position(1, 2),
	7 : Position(1, 3),
	8 : Position(2, 0),
	9 : Position(2, 1),
	10: Position(2, 2),
	11: Position(2, 3),
	12: Position(3, 0),
	13: Position(3, 1),
	14: Position(3, 2),
	15: Position(3, 3),
}

def getNextInSequence(target):
	if (target == 15 or target == 0):
		return -1;
	return correctAnswer[correctAnswerMap[target] + 1];

def getPreviousInSequence(target):
	if (target == 1):
		return -1;
	return correctAnswer[correctAnswerMap[target] - 1];

def loadFileToPieces():
	rawInput = input();
	return [int(piece) for piece in rawInput.split()];

def isPositionValid(pos):
	topBoundary 	= pos.row >= 0;
	bottomBoundary  = pos.row <= 3;
	leftBoundary 	= pos.column >= 0;
	rightBoundary 	= pos.column <= 3;
	return (topBoundary and bottomBoundary and leftBoundary and rightBoundary);

def piecesToBoard(pieces):
	lenX, lenY = 4, 4;
	board = [[0 for x in range(lenX)] for y in range(lenY)];

	board[0][0] = pieces[0];
	board[0][1] = pieces[1];
	board[0][2] = pieces[2];
	board[0][3] = pieces[3];
	board[1][0] = pieces[4];
	board[1][1] = pieces[5];
	board[1][2] = pieces[6];
	board[1][3] = pieces[7];
	board[2][0] = pieces[8];
	board[2][1] = pieces[9];
	board[2][2] = pieces[10];
	board[2][3] = pieces[11];
	board[3][0] = pieces[12];
	board[3][1] = pieces[13];
	board[3][2] = pieces[14];
	board[3][3] = pieces[15];

	return board;

def printBoard(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if (board[i][j] < 10):
				print (str(board[i][j]), end = "  ");
			else:
				print (str(board[i][j]), end = " ");
		print ("\n");

# returns the number of pieces out of place
def heuristicOne(pieces):
	incorrectPieces = 0;
	for index, piece in enumerate(pieces):
		if piece == 0: 
			continue;
		if (piece != correctAnswer[index]):
			incorrectPieces += 1;
	return incorrectPieces;

# returns the number of pieces out of place
def heuristicOneVariation(pieces):
	incorrectPieces = 0;
	for index, piece in enumerate(pieces):
		if (piece != 0 and index != correctAnswerMap[piece]):
			incorrectPieces += 1;
	return incorrectPieces;

# returns the number of pieces out of its sequential order
def heuristicTwo(board):
	incorrectPieces = [];
	row = 0; column = 0;

	while (column < 3):
		currentPiece = board[row][column];
		if (currentPiece == 15 or currentPiece == 0):
			pass;
		elif ((currentPiece + 1) != board[row][column + 1]):
			incorrectPieces.append(currentPiece);
		column += 1;

	while (row < 3):
		currentPiece = board[row][column];
		if (currentPiece == 15 or currentPiece == 0):
			pass;
		elif ((currentPiece + 1) != board[row + 1][column]):
			incorrectPieces.append(currentPiece);
		row += 1;

	while (column != 0):
		currentPiece = board[row][column];
		if (currentPiece == 15 or currentPiece == 0):
			pass;
		elif ((currentPiece + 1) != board[row][column - 1]):
			incorrectPieces.append(currentPiece);
		column -= 1;

	while (row != 1):
		currentPiece = board[row][column];
		if (currentPiece == 15 or currentPiece == 0):
			pass;
		elif ((currentPiece + 1) != board[row - 1][column]):
			incorrectPieces.append(currentPiece);
		row -= 1;

	while (column != 2):
		currentPiece = board[row][column];
		if (currentPiece == 15 or currentPiece == 0):
			pass;
		elif ((currentPiece + 1) != board[row][column + 1]):
			incorrectPieces.append(currentPiece);
		column += 1;

	currentPiece = board[row][column];
	if (currentPiece == 15 or currentPiece == 0):
		pass;
	elif ((currentPiece + 1) != board[row + 1][column]):
		incorrectPieces.append(currentPiece);
	row += 1;

	currentPiece = board[row][column];
	if (currentPiece == 15 or currentPiece == 0):
		pass;
	if ((currentPiece + 1) != board[row][column - 1]):
		incorrectPieces.append(currentPiece);
	column -= 1;

	currentPiece = board[row][column];
	if (currentPiece != 0 and currentPiece != 15):
		incorrectPieces.append(currentPiece);

	return len(incorrectPieces);

# returns the sum of the manhattan distance of each incorrect piece;
def heuristicThree(pieces, board):
	sumDistance = 0;
	for index, piece in enumerate(pieces):
		positionOnBoard = arrayToBoardMap[index];
		correctPosition = correctPositionMap[piece];

		if ((positionOnBoard.row != correctPosition.row) or (positionOnBoard.column != correctPosition.column)):
			sumDistance += abs(positionOnBoard.row - correctPosition.row) + abs(positionOnBoard.column - correctPosition.column);
	return sumDistance;

# returns a combination of the three heuristics multiplied by a weight;
def heuristicFour(pieces, board, weights):
	wOne = heuristicOne(pieces) * weights['p1'];
	wTwo = heuristicTwo(board) * weights['p2'];
	wThree = heuristicThree(pieces, board) * weights['p3'];

	return wOne + wTwo + wThree;



# Init pieces and boards
pieces = loadFileToPieces();
board = piecesToBoard(pieces);
correctBoard = piecesToBoard(correctAnswer);

#printBoard(correctBoard);
#print ("\n")
#printBoard(board);

print ('h1 =', heuristicOne(pieces));
print ('h2 =', heuristicTwo(board));
print ('h3 =', heuristicThree(pieces, correctBoard));
print ('h4 =', heuristicFour(pieces, board, {'p1': 0.2, 'p2': 0.2, 'p3': 0.6}));

