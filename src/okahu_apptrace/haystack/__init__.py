# Copyright (C) Okahu Inc 2023-2024. All rights reserved

import logging
from okahu_apptrace.haystack.wrap_openai import wrap_openai
from okahu_apptrace.haystack.wrap_pipeline import wrap as wrap_pipeline

logger = logging.getLogger(__name__)

HAYSTACK_METHODS = [
    {
        "package": "haystack.components.generators.openai",
        "object": "OpenAIGenerator",
        "method": "run",
        "wrapper": wrap_openai,
    },
    {
        "package": "haystack.components.generators.chat.openai",
        "object": "OpenAIChatGenerator",
        "method": "run",
        "wrapper": wrap_openai,
    },
    {
        "package": "haystack.core.pipeline.pipeline",
        "object": "Pipeline",
        "method": "run",
        "wrapper": wrap_pipeline,
    },
]
