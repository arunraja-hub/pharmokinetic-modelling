import pharmodel as pm

dose_rec = pm.Protocol('test_dosis_combined.csv')
dose_df = dose_rec.read_dosage()
print(dose_df)
model_params = pm.Model(absorb = 1, comp = 0, V_c = 1.0 , CL = .1, Q_p1 = 1.1, V_p1 = 0.1, Q_p2 = 1.0, V_p2 = 0.1, k_a = 1.0)
df_to_solve = pm.Solution(dose_df, model_params)
print(model_params.absorb,model_params.comp)
sol_dataframe = df_to_solve.solve_dataframe(model_params.absorb,model_params.comp)
print('----',sol_dataframe)
vis = pm.Visualisation(sol_dataframe)
vis.plot_figure()