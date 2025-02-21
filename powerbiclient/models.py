#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from enum import IntEnum

# Permissions for embedding Power BI report
class Permissions(IntEnum):
    READ = 0
    READWRITE = 1
    COPY = 2
    CREATE = 4
    ALL = 7

# Types of token for embedding Power BI report
class TokenType(IntEnum):
    AAD = 0
    EMBED = 1

# Embed modes for embedding Power BI report
class EmbedMode(IntEnum):
    VIEW = 0
    EDIT = 1
    CREATE = 2

# Types of data to be exported
class ExportDataType(IntEnum):
    SUMMARIZED = 0
    UNDERLYING = 1