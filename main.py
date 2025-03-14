from app.controllers.user_controller import UserController
from app.controllers.property_controller import PropertyController
from app.controllers.mortgage_controller import MortgageController
from app.controllers.visit_controller import VisitController
from app.controllers.market_analysis_controller import MarketAnalysisController
from app.data.database import db

def menu():
    user_controller = UserController()
    property_controller = PropertyController()
    mortgage_controller = MortgageController()
    visit_controller = VisitController(property_controller)
    market_analysis_controller = MarketAnalysisController(property_controller)
    logged_user = None

    while True:
        print("\n===== Portal de Imóveis =====")
        print("1 - Cadastrar Usuário")
        print("2 - Login")
        print("3 - Cadastrar Propriedade")
        print("4 - Buscar Propriedades")
        print("5 - Calcular Financiamento")
        print("6 - Agendar visita")
        print("7 - Avaliar Propriedade")
        print("8 - Exibir Avaliações")
        print("9 - Análise de Mercado")
        print("10 - Logout")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            name = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            password = input("Digite a senha: ")
            user_type = input("Digite o tipo de usuário (Cliente ou Agente): ")
            user_controller.register_user(name, email, password, user_type)

        elif option == "2":
            logged_user = user_controller.login()

        elif option == "3":
            if logged_user is None:
                print("Erro: Nenhum usuário logado.")
            elif logged_user.user_type != "Agente":
                print("Erro: Apenas agentes podem cadastrar uma propriedade.")
            else:
                title = input("Digite o título da propriedade: ")
                description = input("Digite a descrição da propriedade: ")
                price = float(input("Digite o preço da propriedade: "))
                location = input("Digite a localização da propriedade: ")
                property_type = input("Digite o tipo do imóvel (Casa/Apto/Terreno): ")

                new_property = property_controller.add_property(
                    id=len(db.get_properties()) + 1,
                    title=title,
                    description=description,
                    price=price,
                    location=location,
                    property_type=property_type,
                    user=logged_user
                )

                print(f"Propriedade '{new_property.title}' cadastrada com sucesso!")

        elif option == "4":
            # Buscar propriedades
            print("\n===== Buscar Propriedades =====")
            search_type = input("Buscar por: 1 - Localização | 2 - Tipo | 3 - Faixa de preço: ")

            if search_type == "1":
                location = input("Digite a localização: ")
                results = property_controller.search_property_by_location(location)

            elif search_type == "2":
                property_type = input("Digite o tipo do imóvel (Casa/Apto/Terreno): ")
                results = property_controller.search_property_by_type(property_type)

            elif search_type == "3":
                price_min = float(input("Digite o preço mínimo: "))
                price_max = float(input("Digite o preço máximo: "))
                results = property_controller.search_property_by_price_range(price_min, price_max)

            else:
                print("Opção inválida!")
                continue

            if results:
                print("Propriedades encontradas:")
                for prop in results:
                    print(vars(prop))
            else:
                print("Nenhuma propriedade encontrada.")

        elif option == "5":
            # Calcular Financiamento
            print("\n===== Calcular Financiamento =====")
            price = float(input("Digite o preço do imóvel: "))
            interest_rate = float(input("Digite a taxa de juros anual (em %): "))
            years = int(input("Digite o período de pagamento (em anos): "))

            # Calcula o financiamento diretamente
            mortgage = mortgage_controller.calculate_mortgage(price, interest_rate, years)

            # Exibe o resultado com base no atributo monthly_payment
            print(f"\nO valor da parcela mensal será: R$ {mortgage.monthly_payment:.2f}")

        elif option == "6":
            print("\n===== Agendar Visita =====")
            if logged_user is None:
                print("Erro: Nenhum usuário logado.")
            else:
                property_id = int(input("Digite o ID da propriedade para agendar visita: "))
                date_time = input("Digite a data e hora para a visita (ex: 2025-03-14 10:00): ")

                # Agendar visita
                new_visit = visit_controller.schedule_visit(
                    id=len(db.get_visits()) + 1,
                    client_id=logged_user.id,
                    agent_id=logged_user.id,  # O agente pode ser o próprio usuário logado ou outro
                    property_id=property_id,
                    date_time=date_time
                )

                if new_visit:
                    print("Visita agendada com sucesso!")
                else:
                    print("Erro ao agendar a visita. Verifique a disponibilidade.")

        elif option == "7":
            print("\n===== Avaliar Propriedade =====")
            if logged_user is None:
                print("Erro: Nenhum usuário logado.")
            else:
                property_id = int(input("Digite o ID da propriedade para avaliar: "))
                rating = int(input("Digite a nota de avaliação (1-5): "))

                # Adicionar avaliação à propriedade
                property_controller.add_rating(property_id, logged_user.id, rating)
                print("Avaliação adicionada com sucesso!")

        elif option == "8":
            print("\n===== Exibir Avaliações =====")
            property_id = int(input("Digite o ID da propriedade para exibir avaliações: "))
            ratings = property_controller.get_ratings(property_id)

            if ratings:
                print("Avaliações:")
                for rating in ratings:
                    print(f"Cliente {rating['user_id']} - Nota: {rating['rating']}")
            else:
                print("Nenhuma avaliação encontrada.")

        elif option == "9":
            print("\n===== Análise de Mercado =====")
            location = input("Digite a localização para análise de mercado: ")
            analysis = market_analysis_controller.get_market_analysis(location)

            if analysis:
                print(f"\nPreço Médio: R$ {analysis['avg_price']:.2f}")
                print(f"Número de Imóveis para Venda: {analysis['num_sale']}")
                print(f"Número de Imóveis para Aluguel: {analysis['num_rent']}")
            else:
                print("Nenhuma análise disponível para esta localização.")

        elif option == "10":
            if logged_user:
                print(f"Logout realizado. Até mais, {logged_user.name}!")
                logged_user = None
            else:
                print("Nenhum usuário logado.")

        elif option == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()