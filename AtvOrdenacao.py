import threading
import time
import random


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

def tarefa(nome_thread, sorting_function, lista):
    print(f"Thread {nome_thread} iniciada.")
    start_time = time.time()
    sorting_function(lista)
    end_time = time.time()
    print(f"Thread {nome_thread} concluída. Tempo de execução: {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    lista_aleatoria = random.sample(range(1, 10000), 100)

    lista_bubble = lista_aleatoria[:]
    lista_selection = lista_aleatoria[:]
    lista_merge = lista_aleatoria[:]

    threads = [
        threading.Thread(target=tarefa, args=("Bubble Sort", bubble_sort, lista_bubble)),
        threading.Thread(target=tarefa, args=("Selection Sort", selection_sort, lista_selection)),
        threading.Thread(target=tarefa, args=("Merge Sort", merge_sort, lista_merge))
    ]

    start_time = time.time()  

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()  
    print("Todas as threads concluídas.")
    print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")
