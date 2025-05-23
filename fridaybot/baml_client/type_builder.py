###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import typing
from baml_py.baml_py import FieldType, EnumValueBuilder, EnumBuilder, ClassBuilder
from baml_py.type_builder import TypeBuilder as _TypeBuilder, ClassPropertyBuilder, ClassPropertyViewer, EnumValueViewer
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME


class TypeBuilder(_TypeBuilder):
    def __init__(self):
        super().__init__(classes=set(
          ["Classification","Issue","Message","ThreadMessage",]
        ), enums=set(
          ["MessageType",]
        ), runtime=DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME)


    @property
    def Classification(self) -> "ClassificationAst":
        return ClassificationAst(self)

    @property
    def Issue(self) -> "IssueAst":
        return IssueAst(self)

    @property
    def Message(self) -> "MessageAst":
        return MessageAst(self)

    @property
    def ThreadMessage(self) -> "ThreadMessageAst":
        return ThreadMessageAst(self)





class ClassificationAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Classification")
        self._properties: typing.Set[str] = set([ "message_id",  "message_type", ])
        self._props = ClassificationProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ClassificationProperties":
        return self._props


class ClassificationViewer(ClassificationAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ClassificationProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def message_id(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("message_id"))

    @property
    def message_type(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("message_type"))

    

class IssueAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Issue")
        self._properties: typing.Set[str] = set([ "number",  "title",  "body",  "type", ])
        self._props = IssueProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "IssueProperties":
        return self._props


class IssueViewer(IssueAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class IssueProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def number(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("number"))

    @property
    def title(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("title"))

    @property
    def body(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("body"))

    @property
    def type(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("type"))

    

class MessageAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("Message")
        self._properties: typing.Set[str] = set([ "id",  "content", ])
        self._props = MessageProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "MessageProperties":
        return self._props


class MessageViewer(MessageAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class MessageProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def id(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("id"))

    @property
    def content(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("content"))

    

class ThreadMessageAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.class_("ThreadMessage")
        self._properties: typing.Set[str] = set([ "user_id",  "content", ])
        self._props = ThreadMessageProperties(self._bldr, self._properties)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def props(self) -> "ThreadMessageProperties":
        return self._props


class ThreadMessageViewer(ThreadMessageAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    
    def list_properties(self) -> typing.List[typing.Tuple[str, ClassPropertyViewer]]:
        return [(name, ClassPropertyViewer(self._bldr.property(name))) for name in self._properties]



class ThreadMessageProperties:
    def __init__(self, bldr: ClassBuilder, properties: typing.Set[str]):
        self.__bldr = bldr
        self.__properties = properties

    

    @property
    def user_id(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("user_id"))

    @property
    def content(self) -> ClassPropertyViewer:
        return ClassPropertyViewer(self.__bldr.property("content"))

    



class MessageTypeAst:
    def __init__(self, tb: _TypeBuilder):
        _tb = tb._tb # type: ignore (we know how to use this private attribute)
        self._bldr = _tb.enum("MessageType")
        self._values: typing.Set[str] = set([ "FeatureRequest",  "BugReport",  "Question",  "Uncategorized", ])
        self._vals = MessageTypeValues(self._bldr, self._values)

    def type(self) -> FieldType:
        return self._bldr.field()

    @property
    def values(self) -> "MessageTypeValues":
        return self._vals


class MessageTypeViewer(MessageTypeAst):
    def __init__(self, tb: _TypeBuilder):
        super().__init__(tb)

    def list_values(self) -> typing.List[typing.Tuple[str, EnumValueViewer]]:
        return [(name, EnumValueViewer(self._bldr.value(name))) for name in self._values]


class MessageTypeValues:
    def __init__(self, enum_bldr: EnumBuilder, values: typing.Set[str]):
        self.__bldr = enum_bldr
        self.__values = values

    

    @property
    def FeatureRequest(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("FeatureRequest"))
    

    @property
    def BugReport(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("BugReport"))
    

    @property
    def Question(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("Question"))
    

    @property
    def Uncategorized(self) -> EnumValueViewer:
        return EnumValueViewer(self.__bldr.value("Uncategorized"))
    

    


__all__ = ["TypeBuilder"]