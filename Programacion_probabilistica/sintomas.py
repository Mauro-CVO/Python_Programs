
def Bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A * prob_B_dado_A)/ prob_B

if __name__ == "__main__":
    prob_cancer = 1 / 100000
    prob_sintoma_y_cancer = 1
    prob_sintoma_y_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_y_cancer * prob_cancer) + (prob_sintoma_y_no_cancer * prob_no_cancer)

    prob_cancer_por_sintoma = Bayes(prob_cancer, prob_sintoma_y_cancer, prob_sintoma)
    prob_no_cancer_por_sintoma = Bayes(prob_no_cancer, prob_sintoma_y_no_cancer, prob_sintoma)

    print(prob_cancer_por_sintoma)
    print(prob_no_cancer_por_sintoma)
    print(prob_cancer_por_sintoma + prob_no_cancer_por_sintoma)