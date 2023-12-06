from dataclasses import dataclass
from itertools import chain
import asyncio
"""
It was run with pypy and execution took 3.4h.
"""

@dataclass
class mapping:
    dst: int
    src: int
    cnt: int


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
            vals = [int(x.strip()) for x in vals.split(' ') if x]
            iteration = 0
            ranges = []
            while len(vals):
                iteration += 1
                print(f'{iteration=}')
                ranges.append(range(vals[0], vals[0] + vals[1] + 1))
                vals = vals[2:]
            seeds = chain(*ranges)
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

maps_to_convert = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                   temperature_to_humidity, humidity_to_location]

async def fun(seed):
    for current_map in maps_to_convert:
        for m in current_map:
            if seed in range(m.src, m.src + m.cnt + 1):
                distance = seed - m.src
                seed = m.dst + distance
                break
    return seed


async def main():
    minimum = 999999999999999999999999999999999999999999999999999999999999999999999999999999
    for seed in seeds:
        minimum = min([await fun(seed), minimum])
    print(f'Answer: {minimum}')

asyncio.run(main())