from math import log2

t_t = 0.45
t_f = 0.10
f_t = 0.05
f_f = 0.40

t_1 = 0.55
f_1 = 0.45
t_2 = 0.5
f_2 = 0.5

value = t_t * log2(t_t/(t_1 * t_2)) + t_f * log2(t_f/(t_1 * f_2)) + f_t * log2(f_t/(f_1 * t_2)) + f_f * log2(f_f/(f_1 * f_2))

print(value)