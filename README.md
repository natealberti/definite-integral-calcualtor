# definite-integral-calcualtor
Definite integral calculator using midpoint method

I tried a few times before to create something like this a few times, with little success. Came upon this article (https://towardsdatascience.com/building-a-numerical-integration-tool-in-python-from-scratch-a8185449b70a) and it really helped me figure how to structure the algorithm. After getting it working, I implemented a feature which uses the Equations library to convert a string from the user into an expression, which is then passed through the calculator based on the given limits of integration. To enter the integrand correctly, make sure to put an asterisk in an expression with multiplication like 4*x, or 1/(x*(x+1)), that tripped me up because it was giving errors when I typed stuff like 4x.
