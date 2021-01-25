plotting with pandas 
	pandas itself has built-in methods that simplify  creating
	visulizations from DataFrame and Series objects.
	
	s = pd.Series(np.random.rand(10).cumsum(),
		index=np.arange(1,100,10))
		
	s.plot()
	
Series and DataFrame each have a plot attribute for making some 
basic plot types.By default plot() function draws line plot.

The Series object's is passed to matplotlib for plotting on 
the x-axis, though you can disable this by passing use_index=False.
====================================================================
plotting DataFrame
	DataFrame's plot method plots each of its columns as a different
	line on the same subplot, creating a legend automatically.
	The plot attribute contains a "family" of methods for different
	plot types.
	For Ex:
		df.plot() is equivalent to
		df.plot.line()
		
	arguments
		subplots : plot each dataframe columns in different subplot
					True/False
		sharex	 : if subplots=True share the same x axis,linking 
					ticks and limits.
		sharey	 : if subplots=True share the same y axis
		
		figsize  : size of figure to create as tuple
		title	 : plot title as string
		legend 	 : add a subplot legend(True by default)
		sort_columns : Plot columns in alphabetically order,
				by default use existing column order 
				
	EX:
		
		df = pd.DataFrame(np.random.rand(10,4).cumsum(0),
			columns=['A','B','C','D'],index=np.arange(0,100,10))
		df.plot()