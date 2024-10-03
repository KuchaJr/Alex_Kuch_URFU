#const
positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#Перевод координат шахматной доски в удобный вид
def convert_chess_to_coord(chess_coord):
    y = int(chess_coord[1])
    x = positions.index(chess_coord[0]) + 1
    return x, y
#Проверка каждой фигуры на возможность хода
def check_ability(start_coord, end_coord, figure):
    x1, y1 = convert_chess_to_coord(start_coord)
    x2, y2 = convert_chess_to_coord(end_coord)
    if figure == 'пешка':
        return x1 == x2 and y2 - y1 == 1
    elif figure == 'конь':
        return abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1
    elif figure == 'слон':
        return abs(x1 - x2) == abs(y1 - y2)
    elif figure == 'ладья':
        return x1 == x2 or y1 == y2
    elif figure == 'королева':
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
    elif figure == 'король':
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
piece = input('Введите название фигуры: ')
start, end = map(str, input('Введите начальную и конечную позицию фигуры (через пробел): ').split())
if check_ability(start, end, piece): print(f'{piece} может так ходить.')
else: print(f'{piece} не может так ходить.')