from db.mysql_repository import MysqlRepository

def test_load_orthographies():
    repo = MysqlRepository()
    orthographies = repo.load_orthographies()
    assert 'ß' in orthographies['German']
    assert 'ß' not in orthographies['English']
    assert 'a' in orthographies['English']