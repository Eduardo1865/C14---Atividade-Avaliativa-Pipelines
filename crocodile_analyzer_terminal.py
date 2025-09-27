#!/usr/bin/env python3


import pandas as pd
import os
import sys

class CrocodileAnalyzer:

    
    def __init__(self, csv_file):
        
        self.csv_file = csv_file
        self.data = None
        self.load_data()
    
    def load_data(self):

        try:
            self.data = pd.read_csv(self.csv_file)
            print(f"Dataset carregado com sucesso! {len(self.data)} observações encontradas.\n")
        except FileNotFoundError:
            print(f"Erro: Arquivo {self.csv_file} não encontrado!")
            sys.exit(1)
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            sys.exit(1)
    
    def function_1_basic_info(self):
        print("=" * 60)
        print("INFORMAÇÕES BÁSICAS DO DATASET")
        print("=" * 60)
        print(f"Total de observações: {len(self.data)}")
        print(f"Total de colunas: {len(self.data.columns)}")
        print(f"Tamanho em memória: {self.data.memory_usage(deep=True).sum() / 1024:.2f} KB")
        print(f"\nColunas disponíveis:")
        for i, col in enumerate(self.data.columns, 1):
            print(f"  {i:2d}. {col}")
        print(f"\nTipos de dados:")
        print(self.data.dtypes)
    
    def function_2_species_count(self):
        print("=" * 60)
        print("CONTAGEM POR ESPÉCIE")
        print("=" * 60)
        species_count = self.data['Common Name'].value_counts()
        for i, (species, count) in enumerate(species_count.head(10).items(), 1):
            print(f"{i:2d}. {species:<35} | {count:3d} observações")
        print(f"\nTotal de espécies únicas: {len(species_count)}")
    
    def function_3_size_statistics(self):
        print("=" * 60)
        print("ESTATÍSTICAS DE COMPRIMENTO")
        print("=" * 60)
        length_data = self.data['Observed Length (m)'].dropna()
        print(f"Média: {length_data.mean():.2f} metros")
        print(f"Mediana: {length_data.median():.2f} metros")
        print(f"Desvio padrão: {length_data.std():.2f} metros")
        print(f"Mínimo: {length_data.min():.2f} metros")
        print(f"Máximo: {length_data.max():.2f} metros")
        print(f"1º Quartil: {length_data.quantile(0.25):.2f} metros")
        print(f"3º Quartil: {length_data.quantile(0.75):.2f} metros")
        print(f"Total de medições válidas: {len(length_data)}")
    
    def function_4_weight_statistics(self):
        print("=" * 60)
        print("ESTATÍSTICAS DE PESO")
        print("=" * 60)
        weight_data = self.data['Observed Weight (kg)'].dropna()
        print(f"Média: {weight_data.mean():.2f} kg")
        print(f"Mediana: {weight_data.median():.2f} kg")
        print(f"Desvio padrão: {weight_data.std():.2f} kg")
        print(f"Mínimo: {weight_data.min():.2f} kg")
        print(f"Máximo: {weight_data.max():.2f} kg")
        print(f"1º Quartil: {weight_data.quantile(0.25):.2f} kg")
        print(f"3º Quartil: {weight_data.quantile(0.75):.2f} kg")
        print(f"Total de medições válidas: {len(weight_data)}")
    
    def function_5_habitat_distribution(self):
        print("=" * 60)
        print("DISTRIBUIÇÃO POR HABITAT")
        print("=" * 60)
        habitat_dist = self.data['Habitat Type'].value_counts()
        for i, (habitat, count) in enumerate(habitat_dist.items(), 1):
            percentage = (count / len(self.data)) * 100
            print(f"{i:2d}. {habitat:<25} | {count:3d} ({percentage:5.1f}%)")
    
    def function_6_conservation_status(self):
        print("=" * 60)
        print("STATUS DE CONSERVAÇÃO")
        print("=" * 60)
        conservation = self.data['Conservation Status'].value_counts()
        for status, count in conservation.items():
            percentage = (count / len(self.data)) * 100
            print(f"{status:<20} | {count:3d} ({percentage:5.1f}%)")
    
    def function_7_age_class_analysis(self):
        print("=" * 60)
        print("DISTRIBUIÇÃO POR IDADE")
        print("=" * 60)
        age_dist = self.data['Age Class'].value_counts()
        for age, count in age_dist.items():
            percentage = (count / len(self.data)) * 100
            print(f"{age:<15} | {count:3d} ({percentage:5.1f}%)")
    
    
def show_menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 80)
    print("🐊 ANÁLISE INTERATIVA DO DATASET DE CROCODILOS 🐊")
    print("=" * 80)
    print("Escolha uma das 20 opções de análise:")
    print()
    
    options = [
        "1.  Informações básicas do dataset",
        "2.  Contagem por espécie",  
        "3.  Estatísticas de comprimento",
        "4.  Estatísticas de peso",
        "5.  Distribuição por habitat",
        "6.  Status de conservação",
        "7.  Análise por classe etária",
    ]
    
    
    for i in range(0, len(options), 2):
        left = options[i] if i < len(options) else ""
        right = options[i+1] if i+1 < len(options) else ""
        print(f"{left:<40} {right}")
    
    print()
    print("0.  Sair")
    print("=" * 80)

def main():
    
    csv_file = 'crocodile_dataset.csv'
    if not os.path.exists(csv_file):
        print(f"Arquivo {csv_file} não encontrado no diretório atual!")
        print("Certifique-se de que o arquivo está no mesmo diretório do programa.")
        return
    

    analyzer = CrocodileAnalyzer(csv_file)
    

    functions = {
        1: analyzer.function_1_basic_info,
        2: analyzer.function_2_species_count,
        3: analyzer.function_3_size_statistics,
        4: analyzer.function_4_weight_statistics,
        5: analyzer.function_5_habitat_distribution,
        6: analyzer.function_6_conservation_status,
        7: analyzer.function_7_age_class_analysis,
        
    }
    
    
    while True:
        show_menu()
        
        try:
            choice = input("Digite sua opção (0-20): ").strip()
            
            if choice == '0':
                print("\nObrigado por usar o Analisador de Crocodilos! Até mais!")
                break
            
            choice_int = int(choice)
            
            if choice_int in functions:
                print("\n")
                functions[choice_int]()
                input("\nPressione ENTER para continuar...")
            else:
                print("Opção inválida! Por favor, digite um número de 0 a 20.")
                input("Pressione ENTER para continuar...")
                
        except ValueError:
            print("Por favor, digite apenas números!")
            input("Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário. Até mais!")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()