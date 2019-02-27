import itertools
print(
    0 in list(
        map(
            lambda x: int(x()),
            itertools.repeat(
                input,
                int(
                    input()
                )
            )
        )
    )
)
