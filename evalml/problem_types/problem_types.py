from enum import Enum


class ProblemTypes(Enum):
    """Enum for type of machine learning problem: BINARY, MULTICLASS, or REGRESSION."""
    BINARY = 'binary'
    MULTICLASS = 'multiclass'
    REGRESSION = 'regression'

    def __str__(self):
        problem_type_dict = {ProblemTypes.BINARY.name: "Binary",
                             ProblemTypes.MULTICLASS.name: "Multiclass",
                             ProblemTypes.REGRESSION.name: "Regression"}
        return problem_type_dict[self.name]
