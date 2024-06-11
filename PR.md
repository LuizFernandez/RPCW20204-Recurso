# RPCW20204-Recurso

## Exercicio 1

Class:
- Pessoa
    - Estudante
    - Professor
- Lingua
- Curso
- Universidade

Data Properties:

- Pessoa
    - id_pessoa
    - nome

- Lingua
    - id_lingua
    - lingua

- Curso
    - id_curso
    - curso

- Universidade
    - id_universidade
    - universidade

Object Properties:

- Professor -> Estuante
    - professor
- Estudante -> Lingua
    - aprende
    - fluente
- Professor -> Lingua
    - ensina
- Estudante -> Curso
    - inscritoEm
- Professor -> Curso
    - lecionaEm
- Estudante -> Universidade
    - estudaNa
- Professor -> Universidade
    - trabalhaNa
- Pessoa -> Pessoa
    - conhece

As queries pedidas estão no ficheiro queries.txt

## Exercicio 2

Correr o ficheiro dataset_clean.py para tratar das listas que estão em string

O script de povoamento não está a funcionar, contudo as queries foram feitas e estão no ficheiro queries.txt