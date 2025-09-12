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

--5.WAQTD name and sal along with annual sal for all employees whose sal is less than blake and more than 3500

SELECT ENAME, SAL, SAL * 12 as ANNUAL_SAL
FROM SCOTT.EMP
WHERE SAL > 3500
and
SAL < (SELECT SAL
        FROM SCOTT.EMP
        WHERE ENAME = 'BLAKE');

--6. WAQTD details of all the employees earning more than scott but less than blake

SELECT *
FROM SCOTT.EMP
WHERE SAL > (SELECT SAL
        FROM SCOTT.EMP
        WHERE ENAME = 'SCOTT')
AND
SAL < (SELECT SAL
        FROM SCOTT.EMP
        WHERE ENAME = 'BLAKE');

--7. WAQTD name of the employees whose name starts with A and wroks as same department as BLAKE 

SELECT ENAME 
FROM EMP 
WHERE ENAME like '%A'
AND DEPTNO = (SELECT DEPTNO
              FROM EMP 
              WHERE ENAME = 'BLAKE');




