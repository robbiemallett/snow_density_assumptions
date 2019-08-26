def speed(density,form):
    """ Return the radar speed from dry snow density
    density can be in g/cm3 or kg/m3
    form can be 'Ulaby','Hallikainen','Tiuri'
    string can be 'speed', 'factor' or 'wrongfactor'
    """
    c = 3e8
    if density > 10:
        density = density/1000
    speed_dict = {"Ulaby" : c*((1+0.51*density)**(-1.5)),
                  "Hallikainen":c*((1+1.91*density)**(-0.5)),
                  "Tiuri":c*((1+1.7*density + 0.7*density**2)**(-0.5))}
    return(speed_dict[form])

def wrong_factor(density,form):
    """ Return the wrong propagation offset from dry snow density
    density can be in g/cm3 or kg/m3
    form can be 'Ulaby','Hallikainen','Tiuri'
    """
    c = 3e8
    if density > 10:
        density = density/1000
    speed_dict = {"Ulaby" : c*((1+0.51*density)**(-1.5)),
                  "Hallikainen":c*((1+1.91*density)**(-0.5)),
                  "Tiuri":c*((1+1.7*density + 0.7*density**2)**(-0.5))}
    speed = speed_dict[form]
    return(1-(speed/c))

def factor(density,form):
    """ Return the propagation offset from dry snow density
    density can be in g/cm3 or kg/m3
    form can be 'Ulaby','Hallikainen','Tiuri'
    """
    c = 3e8
    if density > 10:
        density = density/1000
    speed_dict = {"Ulaby" : c*((1+0.51*density)**(-1.5)),
                  "Hallikainen":c*((1+1.91*density)**(-0.5)),
                  "Tiuri":c*((1+1.7*density + 0.7*density**2)**(-0.5))}
    speed = speed_dict[form]
    return((c/speed)-1)
