original_list = [
    "pbj", "shroom", "carter", "osc", "toob", "nothing",
    "nuke", "amogus", "flash", "winrar", "smile_ghost",
    "ohl", "idiot", "crying_sans", "metal_pipe", "meem",
    "darkness", "jet", "intruder", "bear", "grumbo",
    "giggle", "rei", "leorio", "mohu", "jack",
    "unfortunate", "nope", "noob", "observer",
    "benny", "racoon", "fazmug", "donot",
    "bear5", "fan", "smurf_cat", "blabber",
    "chilly", "little_gerry", "subspace_tripmine",
    "boykisser", "boba", "squewe", "ccat", "smiler",
    "inhabitant", "leoret", "dread", "andy", "catnap", "mrl", "trespasser", "anim8or", "pool_noodle"
]

unicode_chars = [
"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", ""
]

for item, char in zip(original_list, unicode_chars):
    print(f"#> {item}")
    print(f"title @a[tag={item}_d] times 0 5 20")
    print(f'execute at @a[tag={item}_d] if score @p nn_jumpscare matches 1 run title @p title {{"text":" {char}","color":"red"}}')
    print(f'execute at @a[tag={item}_d] if score @p nn_jumpscare matches 2 run title @p title {{"text":"{char}    "}}')
    print(f'execute at @a[tag={item}_d] if score @p nn_jumpscare matches 3 run title @p title {{"text":"{char}","color":"red"}}')
    print(f'execute at @a[tag={item}_d] if score @p nn_jumpscare matches 3 run scoreboard players add @p nn_jumpscare_run 10')
    print(f'# execute at @a[tag={item}_d] if score @p nn_jumpscare matches 3 run title @p title {{"text":"{char}","color":"red"}}')
    print()
