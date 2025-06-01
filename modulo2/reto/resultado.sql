-- 3 La información de los empleados ordenados por nombre (firstName).
select *
from classicmodels.employees e 
order by e.firstName

-- 4 Los países donde hay oficinas (sin duplicar).
select distinct ( o.country)
from classicmodels.offices o 

--  5 El nombre y teléfono de los clientes de la ciudad de Nueva York (NYC).
select c.customerName , c.phone 
from classicmodels.customers c 
where c.city = 'NYC'

-- 6 El código y nombre de los productos del vendedor Gearbox Collectibles que tengan menos de 1000 unidades en stock.
select p.productCode as CODIGO_PRODUCTO, p.productName  as NOMBRE_VENDEDOR
from classicmodels.products p 
where p.productVendor = 'Gearbox Collectibles' and p.quantityInStock  < 1000

-- 7 Los tres productos más caros, desde el punto de visto de los comercializadores (buyPrice).
select p.productName , p.buyPrice
from classicmodels.products p 
order by p.buyPrice desc
limit 3

-- 8 La cantidad de productos por línea de producto (no las existencias en inventario)
select pd.productLine as LINEA_PRODUCTO, count(*) as CANTIDAD
from classicmodels.products pd 
group by pd.productLine 


-- 9 La cantidad de empleados por país (tomando en cuenta la ubicación de la oficina).
SELECT o.country as PAIS, COUNT(*) as CANTIDAD
FROM classicmodels.employees e, classicmodels.offices o 
WHERE e.officeCode = o.officeCode
GROUP BY o.country;

-- con join
SELECT o.country, COUNT(*) AS cantidad_empleados
FROM classicmodels.employees e
JOIN classicmodels.offices o ON e.officeCode = o.officeCode
GROUP BY o.country;

-- 10 El promedio de los pagos de cada uno de los clientes de España (sin incluir aquellos que no poseen ningún pago).
select c.customerName , AVG(od.priceEach * od.quantityOrdered)
from classicmodels.customers c , classicmodels.orders o , classicmodels.orderdetails od
where o.customerNumber = c.customerNumber and o.orderNumber = od.orderNumber and c.country = 'Spain' 
group by c.customerName

-- 10. Promedio de los pagos de cada cliente de España (sin incluir clientes sin pagos)
SELECT 
  c.customerName,
  AVG(p.amount) AS promedio_pago
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
WHERE c.country = 'Spain'
GROUP BY c.customerName;




