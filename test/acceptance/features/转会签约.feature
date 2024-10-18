# Created by Administrator at 2024/10/16
Feature: 运动员提出转会申请,总经理审批通过,队医提交体检结果后,球员签合同完成转会
  # Enter feature description here
  AS 联赛方主管
  I WANT TO 管理足球运动员的转会流程
  SO THAT 让转会流程信息化管理更加合规可靠

  Scenario: 运动员"范志毅"提起转会申请
    # Enter steps here
#    Given 运动员处在转会期
    When 运动员提交转会申请
      | 运动员姓名 | 目标俱乐部 |
      | 范志毅   | 上海申花队 |
    And 总经理审批通过
    And 队医提交体检结果
    And 球员签合同完成转会
    Then "范志毅"转会至"上海申花队"