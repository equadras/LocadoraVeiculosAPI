// Criar nós para veículos
CREATE 
  (v1:Veiculo {placa: 'ABC1234', tipo_comb: 'Gasolina', cor: 'Preto', marca: 'Toyota', modelo: 'Corolla', kms: 50000, vlr_car: 35000.00, ar_cond: true, ativo: true}),
  (v2:Veiculo {placa: 'DEF5678', tipo_comb: 'Etanol', cor: 'Prata', marca: 'Chevrolet', modelo: 'Onix', kms: 40000, vlr_car: 30000.00, ar_cond: false, ativo: true}),
  (v3:Veiculo {placa: 'GHI91011', tipo_comb: 'Diesel', cor: 'Branco', marca: 'Ford', modelo: 'Ranger', kms: 60000, vlr_car: 50000.00, ar_cond: true, ativo: true}),
  (v4:Veiculo {placa: 'JKL3456', tipo_comb: 'Flex', cor: 'Vermelho', marca: 'Volkswagen', modelo: 'Gol', kms: 40000, vlr_car: 28000.00, ar_cond: true, ativo: true}),
  (v5:Veiculo {placa: 'MNO6789', tipo_comb: 'Gasolina', cor: 'Branco', marca: 'Chevrolet', modelo: 'Prisma', kms: 35000, vlr_car: 25000.00, ar_cond: false, ativo: true}),
  (v6:Veiculo {placa: 'PQR9012', tipo_comb: 'Diesel', cor: 'Cinza', marca: 'Ford', modelo: 'Fiesta', kms: 45000, vlr_car: 30000.00, ar_cond: true, ativo: true});

// Criar nós para funcionários
CREATE 
  (f1:Funcionario {nome: 'João Silva', cpf: '12345678901', cargo: 'Mecânico', endereco: 'Rua das Flores, 123', salario: 2500.00, dt_nasc: date('1990-05-15'), ativo: true}),
  (f2:Funcionario {nome: 'Maria Santos', cpf: '98765432109', cargo: 'Atendente', endereco: 'Av. Principal, 456', salario: 2000.00, dt_nasc: date('1995-10-20'), ativo: true}),
  (f3:Funcionario {nome: 'José Oliveira', cpf: '45678912306', cargo: 'Gerente', endereco: 'Rua das Palmeiras, 789', salario: 3500.00, dt_nasc: date('1985-03-25'), ativo: true}),
  (f4:Funcionario {nome: 'Mariana Oliveira', cpf: '78901234567', cargo: 'Secretária', endereco: 'Rua das Flores, 456', salario: 1800.00, dt_nasc: date('1992-08-20'), ativo: true}),
  (f5:Funcionario {nome: 'Carlos Silva', cpf: '34567890123', cargo: 'Atendente', endereco: 'Av. Central, 789', salario: 2000.00, dt_nasc: date('1993-05-10'), ativo: true}),
  (f6:Funcionario {nome: 'Leticia Santos', cpf: '90123456789', cargo: 'Mecânica', endereco: 'Rua dos Coqueiros, 123', salario: 2200.00, dt_nasc: date('1991-12-15'), ativo: true});

// Criar nós para clientes
CREATE 
  (c1:Cliente {nome: 'Ana Souza', cpf: '78945612302', endereco: 'Av. das Oliveiras, 789', dt_nasc: date('1998-01-20'), cnh: '123456789'}),
  (c2:Cliente {nome: 'Pedro Rocha', cpf: '65498732105', endereco: 'Rua das Pedras, 456', dt_nasc: date('1980-09-05'), cnh: '987654321'}),
  (c3:Cliente {nome: 'Carla Lima', cpf: '32165498708', endereco: 'Travessa das Flores, 123', dt_nasc: date('1975-12-10'), cnh: '654321987'});

// Criar nós para reservas e relacionamentos
CREATE 
  (res1:Reserva {valor: 150.00, dt_reserva: date('2024-05-10'), dt_devolucao: date('2024-05-15')}),
  (res2:Reserva {valor: 200.00, dt_reserva: date('2024-06-01'), dt_devolucao: date('2024-06-07')}),
  (res3:Reserva {valor: 180.00, dt_reserva: date('2024-07-20'), dt_devolucao: date('2024-07-25')});

// Criar relacionamentos entre reservas, clientes e funcionários
MATCH (res1:Reserva), (c1:Cliente), (f2:Funcionario)
WHERE res1.valor = 150.00 AND c1.nome = 'Ana Souza' AND f2.nome = 'Maria Santos'
CREATE (c1)-[:FEZ_RESERVA]->(res1), (f2)-[:ATENDEU_RESERVA]->(res1);

MATCH (res2:Reserva), (c2:Cliente), (f3:Funcionario)
WHERE res2.valor = 200.00 AND c2.nome = 'Pedro Rocha' AND f3.nome = 'José Oliveira'
CREATE (c2)-[:FEZ_RESERVA]->(res2), (f3)-[:ATENDEU_RESERVA]->(res2);

MATCH (res3:Reserva), (c3:Cliente), (f1:Funcionario)
WHERE res3.valor = 180.00 AND c3.nome = 'Carla Lima' AND f1.nome = 'João Silva'
CREATE (c3)-[:FEZ_RESERVA]->(res3), (f1)-[:ATENDEU_RESERVA]->(res3);

// Criar relacionamentos entre reservas e veículos
MATCH (res1:Reserva), (v1:Veiculo)
WHERE v1.placa = 'ABC1234'
CREATE (res1)-[:RESERVOU_VEICULO]->(v1);

MATCH (res2:Reserva), (v2:Veiculo)
WHERE v2.placa = 'DEF5678'
CREATE (res2)-[:RESERVOU_VEICULO]->(v2);

MATCH (res3:Reserva), (v3:Veiculo)
WHERE v3.placa = 'GHI91011'
CREATE (res3)-[:RESERVOU_VEICULO]->(v3);

