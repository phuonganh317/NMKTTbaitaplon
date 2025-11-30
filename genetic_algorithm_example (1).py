import random

# Tham số thuật toán
POP_SIZE = 8      # Kích thước quần thể
CHROM_LENGTH = 5  # Số bit cho mỗi cá thể (tương ứng x ∈ [0, 31])
GENERATIONS = 20  # Số thế hệ

def fitness(x):
    return x ** 2  # Hàm mục tiêu

def decode(chrom):
    # Chuyển binary sang số nguyên
    return int("".join(str(gene) for gene in chrom), 2)

def create_chromosome():
    # Sinh cá thể ngẫu nhiên (dãy bit)
    return [random.randint(0, 1) for _ in range(CHROM_LENGTH)]

def crossover(parent1, parent2):
    # Lai ghép 1 điểm cắt
    point = random.randint(1, CHROM_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chrom, mutation_rate=0.1):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in chrom]

# Khởi tạo quần thể
population = [create_chromosome() for _ in range(POP_SIZE)]

for gen in range(GENERATIONS):
    # Đánh giá fitness
    decoded = [decode(chrom) for chrom in population]
    fit_values = [fitness(x) for x in decoded]
    
    # Chọn lọc (chọn 4 cá thể tốt nhất)
    sorted_population = [chrom for _, chrom in sorted(zip(fit_values, population), key=lambda x: x[0], reverse=True)]
    population = sorted_population[:4]
    
    # Tạo quần thể mới bằng lai ghép và đột biến
    new_population = population[:]
    while len(new_population) < POP_SIZE:
        parents = random.sample(population, 2)
        child1, child2 = crossover(parents[0], parents[1])
        new_population.extend([mutate(child1), mutate(child2)])
    population = new_population[:POP_SIZE]
    
    # In kết quả tốt nhất từng thế hệ
    best = max(decoded)
    print(f"Generation {gen+1}: Best x = {best}, f(x) = {fitness(best)}")

# Kết quả cuối cùng
final_decoded = [decode(chrom) for chrom in population]
best_x = max(final_decoded, key=fitness)
print(f"Best solution: x = {best_x}, f(x) = {fitness(best_x)}")