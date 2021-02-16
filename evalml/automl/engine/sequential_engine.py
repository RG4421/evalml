from copy import copy

from evalml.automl.engine import EngineBase


class SequentialEngine(EngineBase):
    """The default engine for the AutoML search. Evaluates pipelines locally and pipeline batches sequentially."""
    name = "Sequential Engine"

    def evaluate_batch(self, pipelines):
        """ Evaluates a batch of pipelines in order.

        Arguments:
            pipelines (list(PipelineBase)): A batch of pipelines to be fitted and evaluated.
            log_pipeline (bool): If True, log the pipeline and relevant information before evaluation.

        Returns:
            list (int): a list of the new pipeline IDs which were registered with the automl search
        """
        if self.X_train is None or self.y_train is None:
            raise ValueError("Dataset has not been loaded into the engine.")
        new_pipeline_ids = []
        pipelines = copy(pipelines)
        while self._should_continue_callback() and len(pipelines) > 0:
            pipeline = pipelines[0]
            self._pre_evaluation_callback(pipeline)
            evaluation_result = EngineBase.train_and_score_pipeline(pipeline, self.automl, self.X_train, self.y_train)
            new_pipeline_ids.append(self._post_evaluation_callback(pipeline, evaluation_result))
            pipelines.pop(0)
        return new_pipeline_ids