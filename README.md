# PUCRIO - MVP Fullstack - BACKEND
Repositório referente ao MVP da disciplina Desenvolvimento Fullstack Básico - Backend

## Database concepts:

```
Table Products {
  id integer [pk, unique, not null, increment]
  name varchar
  value float
  created_at timestamp [default: `now()`]
}

Table Sales {
  id integer [pk, unique, not null, increment]
  created_at timestamp [default: `now()`]
}

Table Sales_Products {
  id integer [pk, unique, not null, increment]
  sale_id integer [unique, not null]
  product_id integer
}

Ref: Products.id - Sales_Products.product_id [delete: cascade, update: cascade]
Ref: Sales.id - Sales_Products.sale_id [delete: cascade, update: cascade]
```

## Database Diagram:

![image](https://github.com/pieroribeiro/pucrio_mvp1_backend/assets/2132546/f17ccc70-0207-4faf-91fd-755ee96a34a6)

## Application Endpoints:

### [GET] [/products] - List all Products
