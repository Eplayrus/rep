Вот исправленный markdown с корректным форматированием:  


# Документация по скрипту

## Создание филиалов

- Создаются три филиала: `branch1`, `branch2` и `branch3`.
- Каждый филиал создается с помощью метода `save()`.

```python
# Создание филиалов
branch1 = Branch(branch_address="Москва, ул. 1905 года, д. 7", shor_name="На 1905 года")
branch1.save()

branch2 = Branch(branch_address="Санкт-Петербург, ул. Марата, д. 13", shor_name="СПБ")
branch2.save()

branch3 = Branch(branch_address="Екатеринбург, ул. 8 марта, д. 25", shor_name="Екатеринбург")
branch3.save()
```

## Создание отделов

- Создаются пять отделов: `departament1`, `departament2`, `departament3`, `departament4` и `departament5`.
- Каждый отдел связывается с соответствующим филиалом при создании.
- Для связи отдела с филиалом используется атрибут `branch`.

```python
# Создание отделов
departament1 = Departament(departament_name="Отдел маркетинга", floor=1)
departament1.branch = branch1
departament1.save()

departament2 = Departament(departament_name="Отдел продаж", floor=1)
departament2.branch = branch1
departament2.save()

departament3 = Departament(departament_name="Отдел IT", floor=2)
departament3.branch = branch2
departament3.save()

departament4 = Departament(departament_name="Отдел финансов", floor=3)
departament4.branch = branch2
departament4.save()

departament5 = Departament(departament_name="Отдел HR", floor=1)
departament5.branch = branch3
departament5.save()
```

## Создание сотрудников

- Создаются 30 сотрудников: `employee1`, ..., `employee29`.
- Каждый сотрудник связывается с соответствующим филиалом при создании.
- Для связи сотрудника с филиалом используется атрибут `branch`.

```python
# Создание сотрудников
employee1 = Employee(
    full_name="Иван Иванов", 
    job_title="Руководитель отдела маркетинга", 
    phone_number="8901234567", 
    birthday="1990-01-01"
)
employee1.branch = branch1
employee1.save()

employee2 = Employee(
    full_name="Петр Петров", 
    job_title="Специалист по продажам", 
    phone_number="8912345678", 
    birthday="1992-02-02"
)
employee2.branch = branch1
employee2.save()

# Добавление оставшихся сотрудников в цикле
for i in range(3, 30):
    employee = Employee(
        full_name=f"Иван Иванов {i}", 
        job_title=f"Руководитель отдела маркетинга {i}", 
        phone_number=f"890123456{i}", 
        birthday=f"1990-01-{i:02d}"
    )
    employee.branch = branch1
    employee.save()

for i in range(3, 30):
    employee = Employee(
        full_name=f"Елена Ермолова {i}", 
        job_title=f"Менеджер по HR {i}", 
        phone_number=f"894567890{i}", 
        birthday=f"1998-05-{i:02d}"
    )
    employee.branch = branch3
    employee.save()
```
```
