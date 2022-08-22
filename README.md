# sync-google-sheet

## 维护的数据源
- [client 里的文件](https://github.com/Tougee/sync-google-sheet/tree/master/client)
- google sheet，暂时不包括俄语和繁体中文

## 流程

### 通过修改[client 里的文件](https://github.com/Tougee/sync-google-sheet/tree/master/client)
- 单独创建一个分支来修改表格里的内容，之后发起该分支 -> `master` 的 pull request
- 合并 PR 之后，会自动生成[各平台所需的字符串](https://github.com/Tougee/sync-google-sheet/tree/master/generated/output)

### 通过修改 google sheet

- 修改 google sheet 内容后，会自动给该项目创建一个`script`分支
- 需用户手动发起 `script` -> `master`的 pull request，会自动把 google sheet 里修改的内容同步到 [client.md](https://github.com/Tougee/sync-google-sheet/blob/master/client.md) 和 [client 文件夹](https://github.com/Tougee/sync-google-sheet/tree/master/client)
- 合并 PR 之后，会自动生成[各平台所需的字符串](https://github.com/Tougee/sync-google-sheet/tree/master/generated/output)

## 注意
因为暂时不支持 [client 里的文件](https://github.com/Tougee/sync-google-sheet/tree/master/client) 同步到 google sheet 的功能，所以除了`俄语`和`繁体中文`，其他部分请修改 google sheet，以保持数据统一性。
