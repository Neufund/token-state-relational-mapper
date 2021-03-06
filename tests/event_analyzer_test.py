import pytest
from .test_data.test_transfer_events import *
from token_state_relational_mapper.mapper import TransferEventAnalyzer
from token_state_relational_mapper.mapper.database import Transfer


ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'


def test_true():
    assert list_of_20_minting_transfer_events.__len__() == 20


def test_analyzing_single_transfer_event():
    analyzer = TransferEventAnalyzer()
    balance_changes = analyzer.get_events(list_with_single_transfer_event)
    assert len(balance_changes) == 1

    change: Transfer = balance_changes[0]
    assert change.amount == 1223211588213989209982694
    assert change.from_address == '0x0000000000000000000000000000000000000000'
    assert change.to_address == '0xF432cEc23b2A0d6062B969467f65669De81F4653'


def test_analyzing_multiple_minting_transfer_events():
    analyzer = TransferEventAnalyzer()
    balance_changes = analyzer.get_events(list_of_20_minting_transfer_events)
    assert len(balance_changes) == 20
    assert all(change.from_address == ZERO_ADDRESS for change in balance_changes)


def test_analyzing_wrong_events():
    analyzer = TransferEventAnalyzer()
    changes = analyzer.get_events(list_with_wrong_event)
    assert len(changes) == 0
