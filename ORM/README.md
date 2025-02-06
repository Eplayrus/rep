������������ �� �������:

**�������� ��������**

*   ��������� ��� �������: `branch1`, `branch2` � `branch3`.
*   ������ ������ ��������� � ������� ������ `save()`.

    ```python
# �������� ��������
branch1 = Branch(branch_address="������, ��. 1905 ����, �. 7", shor_name="�� 1905 ����")
branch1.save()

branch2 = Branch(branch_address="�����-���������, ��. ������, �. 13", shor_name="���")
branch2.save()

branch3 = Branch(branch_address="������������, ��. 8 �����, �. 25", shor_name="������������")
branch3.save()
```

**�������� �������**

*   ��������� ���� �������: `departament1`, `departament2`, `departament3`, `departament4` � `departament5`.
*   ������ ����� ����������� � ��������������� �������� ��� ��������.
*   ��� ����� ������ � �������� ������������ ������� `branch`.

    ```python
# �������� �������
departament1 = Departament(departament_name="����� ����������", floor=1)
departament1.branch = branch=branch1
departament1.save()

departament2 = Departament(departament_name="����� ������", floor=1)
departament2.branch = branch=branch1
departament2.save()

departament3 = Departament(departament_name="����� IT", floor=2)
departament3.branch = branch=branch2
departament3.save()

departament4 = Departament(departament_name="����� ��������", floor=3)
departament4.branch = branch=branch2
departament4.save()

departament5 = Departament(departament_name="����� HR", floor=1)
departament5.branch = branch=branch3
departament5.save()
```

**�������� �����������**

*   ��������� 30 �����������: `employee1`, ..., `employee29`.
*   ������ ��������� ����������� � ��������������� �������� ��� ��������.
*   ��� ����� ���������� � �������� ������������ ������� `branch`.

    ```python
# �������� �����������
employee1 = Employee(full_name="���� ������", job_title="������������ ������ ����������", phone_number="8901234567", birthday="1990-01-01")
employee1.branch = branch1
employee1.save()

employee2 = Employee(full_name="���� ������", job_title="���������� �� ��������", phone_number="8912345678", birthday="1992-02-02")
employee2.branch = branch1
employee2.save()

# ...

for i in range(2, 30):
    employee = Employee(full_name=f"���� ������ {i}", job_title=f"������������ ������ ���������� {i}", phone_number=f"890123456{i}", birthday=f"1990-01-0{i}")
    employee.branch = branch1
    employee.save()

# ...

for i in range(2, 30):
    employee = Employee(full_name=f"����� �������� {i}", job_title=f"�������� �� HR {i}", phone_number=f"894567890{i}", birthday=f"1998-05-0{i}")
    employee.branch = branch3
    employee.save()
```

