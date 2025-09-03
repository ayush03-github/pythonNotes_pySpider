**Practice where clause in ORACLE SQL :**



1. WAQTD the annual salary of employee whose name is smith

select SAL*12

from EMP

where ENAME = 'SMITH';



2. WAQTD name of the employee working as a clerk



SELECT ENAME 

FROM EMP

WHERE JOB = 'CLERK';



3. WAQTD salary of the employee who are working as salesman



select SAL 

from EMP

where JOB = 'SALESMAN';



4. WAQTD details of employee who earns more than 2000



select * 

from EMP

where SAL > 2000;



5. WAQTD the details of employee whose name is jones



select * 

from EMP

where ENAME = 'JONES';



6. WAQTD the details of the employees hired after 01-JAN-81



SELECT * 

FROM EMP 

WHERE HIREDATE > '31-DEC-80';



7. WAQTD name and salary along with annual salary if the annual salary is more than 12000



SELECT ENAME, SAL, SAL*12 as ANNUAL\_SAL

FROM EMP

WHERE SAL*12 > 12000;



8. WAQTD EMPNO of the employee who are working in dept 30



SELECT EMPNO

FROM EMP

WHERE DEPTNO = 30;



9. WAQTD ENAME and HIREDATE if they are hired before 81



SELECT ENAME, HIREDATE

FROM EMP 

WHERE HIREDATE < '01-JAN-81';



10. WAQTD details of the employees working as MANAGER



SELECT *

FROM EMP

WHERE JOB = 'MANAGER';



11. WAQTD NAME and SALARY given to an employee if the employee earns a commission of rupees 1400?



SELECT ENAME, SAL

FROM EMP

WHERE COMM = 1400;



12. WAQTD details of the employees having commission more than salary



SELECT *

FROM EMP

WHERE COMM > SAL;



13. WAQTD EMPNO of employee hired before the year 87



SELECT EMPNO 

FROM EMP

WHERE HIREDATE < '01-JAN-87';



14. WAQTD details of employees working as an ANALYST.



SELECT *

FROM EMP

WHERE JOB = 'ANALYST';



15. WAQTD details of employees earning more than 2000 rupees?



SELECT *

FROM EMP

WHERE SAL > 2000;











