songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Pavement', 'Shady Lane'),
    ('Plastic Clap', 'Dongle Mojo'),
    ('Mote', 'Pearls')
}

not_nickelback = [tup for tup in songs if tup[0] != 'Nickelback']
print(not_nickelback)

import code
code.interact(local=locals())
