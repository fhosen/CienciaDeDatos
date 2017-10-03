
def bins_scott(electrode):
    diff = max(electrode) - min(electrode)
    div = 3.5*np.std(electrode)*len(electrode)**(-1/3)
    return diff/div