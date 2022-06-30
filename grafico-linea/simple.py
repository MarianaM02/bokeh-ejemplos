from bokeh.plotting import figure, show

# 1. Preparar los datos
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# 2. Crear un nuevo grafico con un titulo y ejes con nombres
p = figure(title="Multiple line example", x_axis_label="x", y_axis_label="y")

# 3. Añadir múltiples renders (renderizadores)
p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
p.line(x, y2, legend_label="Rate", color="red", line_width=2)
p.line(x, y3, legend_label="Objects", color="green", line_width=2)

# 4. Mostrar los resultados
show(p)