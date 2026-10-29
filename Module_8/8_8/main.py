# обратный цикл
start = 0       # начало всегда положительное
end = 9         # конец меньше начала
step = 2        # всегда минус

if end > start:
    start, end = end, start
elif end == start:
    end *= -1
if start < 0:
    start *= -1
if step > 0:
    step *= -1

x_count = abs(( start - (end + step) ) // step)
print(f"количество итераций: {x_count}")
last_x = (start - step) - (abs(step) * x_count)
print(f"последний x: {last_x}")

loop_from = start
loop_to = end
if last_x == end:
    loop_to += step
else:
    print(f"последний x({last_x}) меньше конца({end}). уменьшаем конец цикла на один шаг.\n")

for x in range(loop_from, loop_to, step):
    if x < end:
        print(f"x={x} меньше конца({end}). (предупреждение)")
    y = x**3 + 2 * x**2 - 4 * x + 1
    print(f"В точке {x} функция равна {y}")