v1.0.0:
create operations

  - create new genome store
  - create new chromosome store in existing genome
  - create new chromosome data in chromosome store

select operations

  - get chromosome base pairs length
  - get number of base pairs before matching sequence
  - get x base pairs after matching sequence
  - get x base pairs before matching sequence
  - get x base pairs after y base pairs
  - get x base pairs before y base pairs
  
insert operations

  - append chromosome data
  - prepend chromosome data
  
delete operations

  - delete full genome store
  - delete full chromosome store from genome
  - delete all chromosome data store from genome
  
v2.0.0:
optional insert operations

  - insert data after every sequence match
  - insert data before every sequence match
  - insert data after n-th sequence match
  - insert data before n-th sequence match
  - insert data after y base pairs
  - insert data before y base pairs
  
optional delete operations

  - delete x base pairs after every sequence match
  - delete x base pairs before every sequence match
  - delete x base pairs after n-th sequence match
  - delete x base pairs before n-th sequence match
  - delete x base pairs after y base pairs
  - delete x base pairs before y base pairs
  