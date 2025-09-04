--1. WAQTD employe name and salary of employee earning more tha miller and less than allen
SELECT ENAME, SAL 
FROM SCOTT.EMP
WHERE SAL > (SELECT SAL
            FROM SCOTT.EMP
            WHERE ENAME='MILLER')
            AND
      SAL < (SELECT SAL
            FROM SCOTT.EMP
            WHERE ENAME= 'ALLEN');
--2. WAQTD details of the employees working in department 20 and same designation as smith

SELECT * 
FROM SCOTT.EMP
WHERE DEPTNO = 20 
AND 
JOB = (SELECT JOB
        FROM SCOTT.EMP
        WHERE ENAME = 'SMITH');

--3. WAQTD details of employees working as manager and in same department as turner

SELECT *
FROM SCOTT.EMP
WHERE JOB = 'MANAGER'
AND
DEPTNO = (SELECT DEPTNO
          FROM SCOTT.EMP
          WHERE ENAME ='TURNER');

--4. WAQTD name and HIREDATE of EMPLOYEE hired after 1980 and before king

SELECT ENAME , SAL
FROM SCOTT.EMP
WHERE HIREDATE > TO_DATE('31-DEC-1980','DD-MON-YYYY')
AND
HIREDATE < (SELECT HIREDATE
            FROM SCOTT.EMP
            WHERE ENAME = 'KING');