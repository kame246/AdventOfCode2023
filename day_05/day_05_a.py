from dataclasses import dataclass

@dataclass
class mapping:
    dst:int
    src:int
    cnt:int
    
with open(r'real_data.txt') as f:
    def create_mapping():
        mappings = []
        for line in f:
            if line.strip() == '':
                break
            else:
                vals = [int(x.strip()) for x in line.split(' ') if x]
            mappings.append(mapping(*vals))
        return mappings

    for line in f:
        if line.startswith('seeds:'):
            _, vals = line.split(':')
            seeds = [int(x.strip()) for x in vals.split(' ') if x]
        elif line.startswith('seed-to-soil map'):
            seed_to_soil = create_mapping()
        elif line.startswith('soil-to-fertilizer map'):
            soil_to_fertilizer = create_mapping()
        elif line.startswith('fertilizer-to-water map'):
            fertilizer_to_water = create_mapping()
        elif line.startswith('water-to-light map'):
            water_to_light = create_mapping()
        elif line.startswith('light-to-temperature map'):
            light_to_temperature = create_mapping()
        elif line.startswith('temperature-to-humidity map'):
            temperature_to_humidity = create_mapping()
        elif line.startswith('humidity-to-location map'):
            humidity_to_location = create_mapping()

maps_to_convert = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
for current_map in maps_to_convert:
    mapped_seed = []
    for seed in seeds:
        for m in current_map:
            if seed in range(m.src, m.src + m.cnt + 1):
                distance = seed - m.src
                mapped_seed.append(m.dst + distance)
                break
        else:
            mapped_seed.append(seed)
    seeds = mapped_seed

print(f'Answer: {min(seeds)}') # 21821