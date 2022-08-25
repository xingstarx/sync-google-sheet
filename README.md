# sync-google-sheet

## 维护的数据源
- [client 里的文件](https://github.com/Tougee/sync-google-sheet/tree/master/client)
- google sheet，暂时不包括俄语和繁体中文

## 修改字符串流程（以下2选1即可）

### 通过修改[client 里的文件](https://github.com/Tougee/sync-google-sheet/tree/master/client)
- 单独创建一个分支来修改表格里的内容，之后发起该分支 -> `master` 的 pull request
- 合并 PR 之后，会自动生成[各平台所需的字符串](https://github.com/Tougee/sync-google-sheet/tree/master/generated/output)

### 通过修改 google sheet

- 修改 google sheet 内容后，会自动给该项目创建一个`script`分支
- 需用户手动发起 `script` -> `master`的 pull request，会自动把 google sheet 里修改的内容同步到 [client.md](https://github.com/Tougee/sync-google-sheet/blob/master/client.md) 和 [client 文件夹](https://github.com/Tougee/sync-google-sheet/tree/master/client)
- 合并 PR 之后，会自动生成[各平台所需的字符串](https://github.com/Tougee/sync-google-sheet/tree/master/generated/output)

## 注意
因为暂时不支持 [client 里的文件](https://github.com/Tougee/sync-google-sheet/tree/master/client) 同步到 google sheet 的功能，所以
 - `俄语`和`繁体中文`请修改 [client 里的文件](https://github.com/Tougee/sync-google-sheet#%E9%80%9A%E8%BF%87%E4%BF%AE%E6%94%B9client-%E9%87%8C%E7%9A%84%E6%96%87%E4%BB%B6)
 - 其他语言请 [通过 google sheet 修改](https://github.com/Tougee/sync-google-sheet#%E9%80%9A%E8%BF%87%E4%BF%AE%E6%94%B9-google-sheet)

如果项目中用到的[平台生成工具](https://github.com/MixinNetwork/handsaw)出现 bug，那么修改完 bug 之后可手动运行[生成平台字符串的脚本](https://github.com/Tougee/sync-google-sheet/actions/workflows/manual_generate.yml)
