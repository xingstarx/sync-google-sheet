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


## Google sheet 关联步骤

创建 Google Sheet 到设置自动化的完整流程：

### 1. 创建 Google Sheet
1. 访问 [Google Drive](https://drive.google.com)
2. 点击左上角的"新建" → "Google 表格"
3. 给表格一个合适的名字（点击左上角的"无标题的电子表格"进行重命名）

### 2. 设置 Google Apps Script
1. 在 Google Sheet 中点击"扩展程序" → "Apps Script"
2. 在打开的 Apps Script 编辑器中，将默认的 `myFunction` 替换为你的代码
3. 示例代码（根据你的需求）：
```javascript
function onSheetEdit(e) {
  // 获取当前活动的表格
  const sheet = SpreadsheetApp.getActiveSheet();
  // 获取最后一行
  const lastRow = sheet.getLastRow();
  // 获取最后一列
  const lastColumn = sheet.getLastColumn();
  
  // 获取数据范围
  const range = sheet.getRange(1, 1, lastRow, lastColumn);
  const values = range.getValues();
  
  // 导出为 XLSX
  exportSheetToXLSX();
}

function exportSheetToXLSX() {
  // 你的导出逻辑
}
```

### 3. 设置触发器
1. 在 Apps Script 编辑器中，点击左侧的"触发器"图标（闹钟样式）
2. 点击右下角的"添加触发器"
3. 设置触发器：
   - 选择要运行的函数：`onSheetEdit`
   - 选择部署：`测试版本`
   - 事件源：`来自电子表格`
   - 事件类型：`编辑时`
4. 点击保存，并授予必要的权限

### 4. 设置 GitHub 仓库
1. 在 GitHub 创建新仓库
2. 设置 GitHub Actions：
   - 在仓库中创建 `.github/workflows` 目录
   - 创建 workflow 文件（例如 `sync.yml`）：
```yaml
name: Sync Google Sheet

on:
  push:
    paths:
      - '**.xlsx'  # 当 xlsx 文件发生变化时触发

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Configure Git
        run: |
          git config --global user.name 'GitHub Action'
          git config --global user.email 'action@github.com'

      - name: Pull changes
        run: git pull --rebase origin master

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: master
```

### 5. 连接 Apps Script 和 GitHub
1. 在 Apps Script 中添加 GitHub 相关的代码：
```javascript
function pushToGitHub(fileBlob, fileName) {
  // 这里需要你的 GitHub 个人访问令牌
  const GITHUB_TOKEN = '你的GitHub Token';
  const REPO_OWNER = '你的GitHub用户名';
  const REPO_NAME = '仓库名称';
  
  // GitHub API 端点
  const apiUrl = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${fileName}`;
  
  // 构建请求头
  const headers = {
    'Authorization': `token ${GITHUB_TOKEN}`,
    'Accept': 'application/vnd.github.v3+json'
  };
  
  // 发送请求到 GitHub
  const response = UrlFetchApp.fetch(apiUrl, {
    method: 'PUT',
    headers: headers,
    payload: JSON.stringify({
      message: 'Update from Google Sheet',
      content: Utilities.base64Encode(fileBlob.getBytes()),
      branch: 'master'
    })
  });
}
```

### 6. 获取必要的令牌和权限
1. 创建 GitHub 个人访问令牌：
   - 访问 GitHub Settings → Developer settings → Personal access tokens
   - 生成新令牌，确保有适当的权限（repo 权限）
2. 在 Apps Script 中保存令牌：
   - 使用 Properties Service 存储令牌
   - 或直接在代码中使用（不推荐）

### 7. 测试流程
1. 在 Google Sheet 中做一些修改
2. 检查 Apps Script 执行日志是否有错误
3. 检查 GitHub 仓库是否正确更新
4. 检查 GitHub Actions 是否正常运行

### 注意事项：
1. 确保所有权限都正确设置
2. 保护好你的令牌和敏感信息
3. 考虑添加错误处理和日志记录
4. 考虑添加重试机制
5. 定期检查和维护自动化流程

