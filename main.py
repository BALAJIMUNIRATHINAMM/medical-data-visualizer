import medical_data_visualizer

# Load data
df = medical_data_visualizer.load_and_preprocess_data()

# Generate plots
fig1 = medical_data_visualizer.draw_cat_plot(df)
fig2 = medical_data_visualizer.draw_heat_map(df)

# Show plots
fig1.show()
fig2.show()
