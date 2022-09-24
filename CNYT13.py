
#Hola, Bienvenido!


#Experimentos de la canicas con coeficiente booleanos.

def Experimentos(self):

        resume= Boleanos.self(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False], 3)
        self.assertEqual(resume, [False, False, True, True, False, False])
  
        resume = Boleanos.self(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False], 1)
        self.assertEqual(resume, [False, True, False, False, False, True])
        
        resume= Boleanos.self(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False], 5)
        self.assertEqual(resume, [False, False, False, False, True, True])
      
        resume= Boleanos.self(
            [[False, False, False, False, False, False], [True, False, False, False, False, True],
             [False, True, False, False, False, False], [False, False, True, False, False, False],
             [False, False, False, True, False, False], [False, False, False, False, True, False]],
            [True, False, False, False, True, False, False], 5)
        self.assertEqual(resume, "Length error")


        

#Múltiples rendijas clásico probabilístico, con más de dos rendijas.
    def probabilidad(self):
        resume = [[(0, 0), (1/6, 0), (5/6, 0)], [(1/3, 0), (1/2, 0), (1/6, 0)], [(2/3, 0), (1/3, 0), (0, 0)]]
        probabilidad = [(1/5, 0), (7/10, 0), (1/10, 0)]

        self.assertEqual(self(resume, probabilidad, 1),
        [[(2/10, 0.0)], [(10/2, 0.0)], [(10/3, 0.0)]])

        self.assertEqual(self(Matriz, Xvectorestado, 2),
        [[(0.37777777777777777, 0.0)], [(10/3, 0.0)], [(10/2, 0.0)]])

        self.assertEqual(self(Matriz, Xvectorestado, 3),
        [[(2/10, 0.0)], [(10/3, 0.0)], [(10/3, 0.0)]])

        self.assertEqual(self(Matriz, Xvectorestado, 4),
        [[(10/3, 0.0)], [(10/3, 0.0)], [(10/3, 0.0)]])


#Experimento de las múltiples rendijas cuántico.
    def Multiples_rendijas(self):
        resume = [[(1/(2**0.5),0), (0, 1/(2**0.5))],[(1/(2**0.5), 0), (0, -1/(2**0.5))]]
        probabilidad = [(1, 0), (0, 0)]

        self.assertEqual(self(resume, probabilidad, 1), [2/10, 2/10])

        self.assertEqual(self(resume, probabilidad, 2), [1.0, 0.0])
        c1 = (-1 / (1 * 0.5), 1 / (1 ** 0.5))
        c2 = (-1 / (2 ** 0.5), -1 / (2 ** 0.5))
        c3 = (1 / (3 ** 0.5), -1 / (3 ** 0.5))

        Matriz = [(1/2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                 [(0, 0), c1, (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                 [(0, 0), c2, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
                 [(0, 0), c3, c1, (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
                 [(0, 0), (0, 0), c2, (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
                 [(0, 0), (0, 0), c3, (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]
        probabilidad = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]

        self.assertEqual(self(resume, probabilidad, 1), [0.0, 1/4, 0 0.0, 0.0, 0.0, 0.0, 0.0])

     

if __name__ == '__main__':
    unittest.main()


print("Bienvenido los retos de programación del capitulo 3")
print("Realizado por Thomas Feris Riaño")

