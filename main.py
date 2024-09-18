import random
from collections import defaultdict
from dataclasses import dataclass, field
from typing import TypeAlias, TypedDict

from faker import Faker

T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]

T_USER_NAME: TypeAlias = str


class Human(TypedDict):
    name: T_USER_NAME
    group: T_GROUP_NAME


T_HUMANS: TypeAlias = list[Human]
T_ORGANIZED_DATA: TypeAlias = defaultdict[str, list[str]]
T_OUTPUT: TypeAlias = str


@dataclass
class DataProvider:
    _faker: Faker = field(default_factory=Faker)

    def _generate_group_names(self, amount: int = 10) -> T_GROUP_NAMES:
        return [self._faker.unique.company() for _ in range(amount)]

    def _generate_human(self, group_name: T_GROUP_NAME) -> Human:
        return Human(
            name=self._faker.unique.first_name(),
            group=group_name,
        )

    def _generate_humans(
        self, groups: T_GROUP_NAMES, amount_of_humans: int
    ) -> T_HUMANS:
        members = []
        for _ in range(amount_of_humans):
            group_name = random.choice(groups)
            group_member = self._generate_human(group_name=group_name)
            members.append(group_member)
        return members

    def generate_group_members(
        self, amount_of_groups: int | None = None, amount_of_humans: int | None = None
    ) -> T_HUMANS:
        amount_of_groups = amount_of_groups or random.randint(5, 10)
        amount_of_humans = amount_of_humans or random.randint(3, 30)

        _groups = self._generate_group_names(amount=amount_of_groups)
        return self._generate_humans(
            groups=_groups,
            amount_of_humans=amount_of_humans,
        )


def organize_data(humans: T_HUMANS) -> T_ORGANIZED_DATA:
    organized_dict: T_ORGANIZED_DATA = defaultdict(list)
    for human in humans:
        organized_dict[human["group"]].append(human["name"])
    return organized_dict


def get_formatted_output(data: T_ORGANIZED_DATA) -> T_OUTPUT:
    """
    Get output string that can be used to print in the console.
    """
    result = ""
    for group, members in data.items():
        result += (
            f"In the group {group} "
            f"the number of members is {len(members)}, "
            f"they are: {members}.\n"
        )
    return result


def main() -> None:
    """
    Show all groups with the number and names of members for each group.
    """
    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)


if __name__ == "__main__":
    main()
