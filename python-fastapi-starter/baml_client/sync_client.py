###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Any, Dict, List, Optional, TypeVar, Union, TypedDict, Type, Literal, cast
from typing_extensions import NotRequired
import pprint

import baml_py
from pydantic import BaseModel, ValidationError, create_model

from . import partial_types, types
from .types import Checked, Check
from .type_builder import TypeBuilder
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME

OutputType = TypeVar('OutputType')

# Define the TypedDict with optional parameters having default values
class BamlCallOptions(TypedDict, total=False):
    tb: NotRequired[TypeBuilder]
    client_registry: NotRequired[baml_py.baml_py.ClientRegistry]

class BamlSyncClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __stream_client: "BamlStreamClient"

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__stream_client = BamlStreamClient(self.__runtime, self.__ctx_manager)

    @property
    def stream(self):
      return self.__stream_client

    
    def AnalyzeBooks(
        self,
        input: str,
        baml_options: BamlCallOptions = {},
    ) -> types.BookAnalysis:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "AnalyzeBooks",
        {
          "input": input,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.BookAnalysis, raw.cast_to(types, types))
    
    def AnswerQuestion(
        self,
        question: str,context: types.Context,
        baml_options: BamlCallOptions = {},
    ) -> types.Answer:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "AnswerQuestion",
        {
          "question": question,"context": context,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.Answer, raw.cast_to(types, types))
    
    def ClassifyMessage(
        self,
        convo: List[types.Message],
        baml_options: BamlCallOptions = {},
    ) -> List[types.Category]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ClassifyMessage",
        {
          "convo": convo,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(List[types.Category], raw.cast_to(types, types))
    
    def DescribeCharacter(
        self,
        first_image: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> types.CharacterDescription:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "DescribeCharacter",
        {
          "first_image": first_image,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.CharacterDescription, raw.cast_to(types, types))
    
    def ExtractResume(
        self,
        raw_text: str,
        baml_options: BamlCallOptions = {},
    ) -> types.Resume:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractResume",
        {
          "raw_text": raw_text,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.Resume, raw.cast_to(types, types))
    



class BamlStreamClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager

    
    def AnalyzeBooks(
        self,
        input: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.BookAnalysis, types.BookAnalysis]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "AnalyzeBooks",
        {
          "input": input,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.BookAnalysis, types.BookAnalysis](
        raw,
        lambda x: cast(partial_types.BookAnalysis, x.cast_to(types, partial_types)),
        lambda x: cast(types.BookAnalysis, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    
    def AnswerQuestion(
        self,
        question: str,context: types.Context,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Answer, types.Answer]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "AnswerQuestion",
        {
          "question": question,
          "context": context,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.Answer, types.Answer](
        raw,
        lambda x: cast(partial_types.Answer, x.cast_to(types, partial_types)),
        lambda x: cast(types.Answer, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    
    def ClassifyMessage(
        self,
        convo: List[types.Message],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[List[Optional[types.Category]], List[types.Category]]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ClassifyMessage",
        {
          "convo": convo,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[List[Optional[types.Category]], List[types.Category]](
        raw,
        lambda x: cast(List[Optional[types.Category]], x.cast_to(types, partial_types)),
        lambda x: cast(List[types.Category], x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    
    def DescribeCharacter(
        self,
        first_image: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.CharacterDescription, types.CharacterDescription]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "DescribeCharacter",
        {
          "first_image": first_image,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.CharacterDescription, types.CharacterDescription](
        raw,
        lambda x: cast(partial_types.CharacterDescription, x.cast_to(types, partial_types)),
        lambda x: cast(types.CharacterDescription, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    
    def ExtractResume(
        self,
        raw_text: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Resume, types.Resume]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractResume",
        {
          "raw_text": raw_text,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.Resume, types.Resume](
        raw,
        lambda x: cast(partial_types.Resume, x.cast_to(types, partial_types)),
        lambda x: cast(types.Resume, x.cast_to(types, types)),
        self.__ctx_manager.get(),
      )
    

b = BamlSyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)

__all__ = ["b"]